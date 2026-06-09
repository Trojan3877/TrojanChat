import html
import json
import logging

# Configure defensive security auditing logger
logger = logging.getLogger("TrojanChat.Security")

class BackendSecurityManager:
    """
    Enterprise Security Middleware layer responsible for payload sanitization,
    rate-bounding validation, and input hardening.
    """
    
    # Senior Engineering Threshold Sane Defaults
    MAX_MESSAGE_LENGTH = 4096  # Mitigate RAM exhaustion / Buffer overflow vectors
    MAX_USERNAME_LENGTH = 32   # Block overflow handles
    
    @staticmethod
    def sanitize_string(input_string: str) -> str:
        """
        Strips whitespace and escapes dangerous HTML/script components 
        to completely eliminate downstream XSS execution vectors.
        """
        if not input_string:
            return ""
        
        # 1. Enforce whitespace trimming
        cleaned = input_string.strip()
        
        # 2. Escape HTML special characters (&, <, >, ", ') into secure entities
        return html.escape(cleaned)

    @classmethod
    def validate_and_sanitize_payload(cls, raw_json_bytes: bytes) -> dict:
        """
        Parses, validates, and structurally hardens incoming raw socket packet bytes.
        
        Raises:
            ValueError: If protocol format rules, structural checks, or lengths are violated.
            json.JSONDecodeError: If bytes fail cryptographic/syntax boundaries.
        """
        # 1. Enforce strict JSON compilation boundaries
        payload_str = raw_json_bytes.decode('utf-8')
        data = json.loads(payload_str)
        
        if not isinstance(data, dict):
            logger.warning("Security Exception: Ingested packet is not a valid JSON Object schema.")
            raise ValueError("Malformed packet layout.")

        # 2. Validate structural key existence (Enforce Protocol Layout)
        if "user" not in data or "text" not in data:
            logger.warning("Security Exception: Protocol drop. Mandatory transaction keys missing.")
            raise ValueError("Missing payload keys.")

        raw_user = str(data.get("user", "")).strip()
        raw_text = str(data.get("text", "")).strip()

        # 3. Enforce Data Length Constraints (Defend against Denial of Service floods)
        if len(raw_user) > cls.MAX_USERNAME_LENGTH:
            logger.warning(f"Security Alert: Drop triggered. Username length ({len(raw_user)}) exceeds safety bounds.")
            raise ValueError("Username payload length restriction violation.")
            
        if len(raw_text) > cls.MAX_MESSAGE_LENGTH:
            logger.warning(f"Security Alert: Drop triggered. Message payload length ({len(raw_text)}) exceeds safety bounds.")
            raise ValueError("Message body length restriction violation.")

        # 4. Apply Core Ingestion Sanitization
        sanitized_user = cls.sanitize_string(raw_user)
        sanitized_text = cls.sanitize_string(raw_text)

        if not sanitized_user:
            sanitized_user = "Anonymous"

        return {
            "user": sanitized_user,
            "text": sanitized_text
        }

    @staticmethod
    def audit_security_event(event_type: str, details: str, IP_peer: tuple = None):
        """ Log security exceptions structurally for upstream SIEM parsing dashboards. """
        peer_info = f" from Origin IP: {IP_peer}" if IP_peer else ""
        logger.error(f"[SECURITY_AUDIT] Event: {event_type} | Details: {details}{peer_info}")
