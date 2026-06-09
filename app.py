import os
import sys
import json
import socket
import threading
import subprocess
import streamlit as st

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

SERVER_IP = "127.0.0.1"
SERVER_PORT = 8888

# Thread safe memory lock definition
state_lock = threading.Lock()

@st.cache_resource
def initialize_backend_service():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((SERVER_IP, SERVER_PORT))
            subprocess.Popen(
                [sys.executable, "server.py"], 
                stdout=subprocess.DEVNULL, 
                stderr=subprocess.DEVNULL
            )
            return "Background Chat Engine initialized successfully."
    except socket.error:
        return "Backend Chat Engine already running or port occupied. Binding skipped."

backend_status = initialize_backend_service()

if "messages" not in st.session_state:
    st.session_state.messages = []
if "socket_connected" not in st.session_state:
    st.session_state.socket_connected = False

def tcp_listener_worker(sock):
    """ Continuous background worker tracking delimited streaming network buffers. """
    buffer = ""
    while True:
        try:
            data = sock.recv(4096).decode('utf-8')
            if not data:
                break
            
            buffer += data
            # Cleanly handle sticky TCP packages using our newline delimiter rule
            while "\n" in buffer:
                line, buffer = buffer.split("\n", 1)
                if line.strip():
                    try:
                        payload = json.loads(line)
                        # Thread-Safe Memory Lock Mutation
                        with state_lock:
                            st.session_state.messages.append(payload)
                    except json.JSONDecodeError:
                        continue
        except Exception:
            break
    with state_lock:
        st.session_state.socket_connected = False

st.set_page_config(page_title="TrojanChat Dashboard", page_icon="🛡️", layout="centered")
st.title("🛡️ TrojanChat Production Dashboard")
st.caption(f"Status: {backend_status} | Front/Back Synchronized Interface")

if not st.session_state.socket_connected:
    with st.form("handshake_gateway"):
        st.subheader("Network Handshake Gateway")
        username = st.text_input("Choose your Secure Chat Handle:", value="Corey").strip()
        submit_handshake = st.form_submit_with_button("Establish Socket Handshake")
        
        if submit_handshake and username:
            try:
                client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client_socket.connect((SERVER_IP, SERVER_PORT))
                
                st.session_state.username = username
                st.session_state.client_socket = client_socket
                st.session_state.socket_connected = True
                
                threading.Thread(target=tcp_listener_worker, args=(client_socket,), daemon=True).start()
                st.rerun()
            except ConnectionRefusedError:
                st.error(f"Critical: Core Asynchronous Engine offline at tcp://{SERVER_IP}:{SERVER_PORT}")
else:
    @st.fragment(run_every=1.0)
    def render_live_feed():
        feed_container = st.container(height=420, border=True)
        with feed_container:
            # Thread-safe read mutation
            with state_lock:
                current_messages = list(st.session_state.messages)
                
            if not current_messages:
                st.info("System operational. Transmission channels idle.")
            for msg in current_messages:
                is_me = msg.get("user") == st.session_state.username
                with st.chat_message("user" if is_me else "assistant"):
                    st.markdown(f"**{msg.get('user')}**: {msg.get('text')}")

    render_live_feed()

    if outbound_payload := st.chat_input("Transmit payload package..."):
        if st.session_state.socket_connected:
            packet_data = {
                "user": st.session_state.username,
                "text": outbound_payload
            }
            try:
                # Append delimiter to fix sticky packets at backend ingestion points
                serialized_packet = json.dumps(packet_data) + "\n"
                st.session_state.client_socket.sendall(serialized_packet.encode('utf-8'))
                with state_lock:
                    st.session_state.messages.append(packet_data)
            except Exception:
                st.error("Pipeline failure: Socket context unexpectedly disconnected.")
