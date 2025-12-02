// ============================================
// TrojanChat — Web Client (WebSocket Version)
// ============================================

// Automatically detects backend host OR uses deployment env variable
const API_HOST = window.location.hostname || "localhost";
const WS_URL = `ws://${API_HOST}:8000/ws/chat`;
const HTTP_URL = `http://${API_HOST}:8000`;

// DOM Elements
const messagesDiv = document.getElementById("messages");
const messageInput = document.getElementById("message");
const usernameInput = document.getElementById("username");
const sendButton = document.getElementById("sendBtn");

// Connect WebSocket
let socket = new WebSocket(WS_URL);

// Handle incoming messages
socket.onmessage = function (event) {
    const msg = JSON.parse(event.data);
    appendMessage(msg);
};

// Auto-reconnect if server restarts
socket.onclose = () => {
    setTimeout(() => {
        socket = new WebSocket(WS_URL);
    }, 1000);
};

// Format + append to UI
function appendMessage(msg) {
    const div = document.createElement("div");
    div.classList.add("message");

    const time = msg.timestamp.replace("T", " ").split(".")[0];

    div.innerHTML = `
        <div class="message-username">${msg.username}</div>
        <div class="message-text">${msg.content}</div>
        <div class="message-time" style="font-size: 10px; color: #777; margin-top: 4px;">
            ${time}
        </div>
    `;

    messagesDiv.appendChild(div);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
}

// Fetch initial message history
async function loadHistory() {
    const res = await fetch(`${HTTP_URL}/chat/history?limit=50`);
    const data = await res.json();

    messagesDiv.innerHTML = "";
    data.forEach(appendMessage);
}
loadHistory();

// Send message through WebSocket
function sendMessage() {
    const username = usernameInput.value.trim();
    const content = messageInput.value.trim();

    if (!username || !content) return;

    const msg = {
        username,
        content,
        timestamp: new Date().toISOString()
    };

    socket.send(JSON.stringify(msg));
    messageInput.value = "";
}

// Events
sendButton.addEventListener("click", sendMessage);

messageInput.addEventListener("keypress", (e) => {
    if (e.key === "Enter") sendMessage();
});
