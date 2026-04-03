"""
TrojanChat – Streamlit entry point
Run:  streamlit run streamlit_app.py
"""

import streamlit as st
import pandas as pd
from mcp_adapter import handle_mcp_request, CHAT_HISTORY

st.set_page_config(
    page_title="🏈 TrojanChat",
    page_icon="🏈",
    layout="wide",
)

# ── Sidebar ──────────────────────────────────────────────────────────────────
st.sidebar.title("🏈 TrojanChat")
st.sidebar.markdown("USC Football Real-Time Chat Platform")
st.sidebar.markdown("---")

ROOMS = ["game-day", "recruiting", "staff"]
room = st.sidebar.selectbox("Select Chat Room", ROOMS)
username = st.sidebar.text_input("Your username", value="TrojanFan", max_chars=32)
st.sidebar.markdown("---")

page = st.sidebar.radio("View", ["💬 Chat", "📊 Metrics"])

# ── Chat page ─────────────────────────────────────────────────────────────────
if page == "💬 Chat":
    st.title(f"💬 #{room}")

    # Display existing messages
    messages = handle_mcp_request("fetch_messages", {"room": room, "limit": 50})
    if messages:
        for msg in messages:
            with st.chat_message(msg.get("user", "User")):
                st.markdown(msg.get("message", ""))
                st.caption(msg.get("timestamp", ""))
    else:
        st.info("No messages yet – be the first to post!")

    # Input
    user_input = st.chat_input("Type a message…")
    if user_input:
        result = handle_mcp_request("send_message", {
            "room": room,
            "user": username,
            "message": user_input,
        })
        if result.get("status") == "sent":
            st.rerun()
        else:
            st.error("Message failed to send.")

# ── Metrics page ──────────────────────────────────────────────────────────────
elif page == "📊 Metrics":
    st.title("📊 TrojanChat Performance")

    data = pd.DataFrame({
        "latency_ms": [380, 410, 395, 402, 390, 415],
        "tokens_used": [110, 128, 121, 130, 118, 135],
    })

    col1, col2, col3 = st.columns(3)
    col1.metric("Avg Latency", f"{int(data['latency_ms'].mean())} ms")
    col2.metric("Avg Tokens", f"{int(data['tokens_used'].mean())}")
    col3.metric("Total Rooms", len(ROOMS))

    st.subheader("Latency over time")
    st.line_chart(data["latency_ms"])

    st.subheader("Tokens used over time")
    st.line_chart(data["tokens_used"])

    st.subheader("Message counts per room")
    room_counts = {r: len(CHAT_HISTORY.get(r, [])) for r in ROOMS}
    st.bar_chart(room_counts)
