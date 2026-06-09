import os
import sys
import json
import socket
import threading
import subprocess
import streamlit as st

# Ensure the root directory is on the system path so nested imports resolve cleanly
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Configuration Coordinates (Adjust if deploying to distinct cloud instances)
SERVER_IP = "127.0.0.1"
SERVER_PORT = 8888

# ==============================================================================
# 1. LIFECYCLE MANAGEMENT: AUTO-START BACKEND MICROSERVICE
# ==============================================================================
@st.cache_resource
def initialize_backend_service():
    """ Spins up the server.py asynchronous backbone engine in a detached background process. """
    try:
        # Check if port is already active to prevent port-binding collisions
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((SERVER_IP, SERVER_PORT))
            # If binding succeeds, port was free, meaning server isn't running yet
            process = subprocess.Popen(
                [sys.executable, "server.py"], 
                stdout=subprocess.DEVNULL, 
                stderr=subprocess.DEVNULL
            )
            return "Background Chat Engine initialized successfully."
    except socket.error:
        return "Backend Chat Engine already running or port occupied. Binding skipped."

backend_status = initialize_backend_service()

# ==============================================================================
# 2. STATE PERSISTENCE: SESSION BOUNDARIES
# ==============================================================================
if "messages" not in st.session_state:
    st.session_state.messages = []
if "socket_connected" not in st.session_state:
    st.session_state.socket_connected = False

def tcp_listener_worker(sock):
    """ Continuous background worker thread managing input read buffers from server.py """
    buffer = ""
    while True:
        try:
            data = sock.recv(4096).decode('utf-8')
            if not data:
                break # Remote host hung up cleanly
            
            buffer += data
            # Handle stream-concatenation by splitting cleanly at JSON layout endpoints
            try:
                payload = json.loads(buffer)
                st.session_state.messages.append(payload)
                buffer = "" # Flush buffer on perfect deserialization parse
            except json.JSONDecodeError:
                # Payload chunk incomplete; wait for next frame buffer arrival
                continue
        except Exception:
            break
    st.session_state.socket_connected = False

# ==============================================================================
# 3. INTERFACE PRESENTATION & RENDERING
# ==============================================================================
st.set_page_config(page_title="TrojanChat Dashboard", page_icon="🛡️", layout="centered")
st.title("🛡️ TrojanChat Production Dashboard")
st.caption(f"Status: {backend_status} | Front/Back Synchronized Interface")

# Gateway Authenticator Form
if not st.session_state.socket_connected:
    with st.form("handshake_gateway"):
        st.subheader("Network Handshake Gateway")
        username = st.text_input("Choose your Secure Chat Handle:", value="Corey").strip()
        submit_handshake = st.form_submit_with_button("Establish Socket Handshake")
        
        if submit_handshake and username:
            try:
                # Open a raw streaming socket connection descriptor
                client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client_socket.connect((SERVER_IP, SERVER_PORT))
                
                # Bind references to persistent session state memory
                st.session_state.username = username
                st.session_state.client_socket = client_socket
                st.session_state.socket_connected = True
                
                # Deamonic worker registration to ensure the background listener collapses when app exits
                listener_thread = threading.Thread(target=tcp_listener_worker, args=(client_socket,), daemon=True)
                listener_thread.start()
                st.rerun()
            except ConnectionRefusedError:
                st.error(f"Critical: Core Asynchronous Engine offline at tcp://{SERVER_IP}:{SERVER_PORT}")
else:
    # Isolated Chat Container Rendering Fragment
    @st.fragment(run_every=1.0)
    def render_live_feed():
        """ Auto-polls session memory for new incoming backend traffic every 1.0s without interrupting user typing inputs. """
        feed_container = st.container(height=420, border=True)
        with feed_container:
            if not st.session_state.messages:
                st.info("System operational. Transmission channels idle.")
            for msg in st.session_state.messages:
                # Stylize visually based on sender identity
                is_me = msg.get("user") == st.session_state.username
                with st.chat_message("user" if is_me else "assistant"):
                    st.markdown(f"**{msg.get('user')}**: {msg.get('text')}")

    render_live_feed()

    # Outgoing Payload Core Sender
    if outbound_payload := st.chat_input("Transmit payload package..."):
        if st.session_state.socket_connected:
            packet_data = {
                "user": st.session_state.username,
                "text": outbound_payload
            }
            try:
                # Transmit cleanly over the socket stream buffer
                st.session_state.client_socket.sendall(json.dumps(packet_data).encode('utf-8'))
                # Optimistically register locally to drop rendering wait times down to O(1)
                st.session_state.messages.append(packet_data)
            except Exception:
                st.error("Pipeline failure: Socket context unexpectedly disconnected.")
