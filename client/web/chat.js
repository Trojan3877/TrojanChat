// ==============================================
// TrojanChat — Web Client Logic (Modern Version)
// ==============================================

// Backend URL (change this if deployed)
const API_URL = "http://localhost:8000";

const messagesDiv = document.getElementById("messages");
const messageInput = document.getElementById("message");
const usernameInput = document.getElementById("username");
const sendButton = document.getElementById("sendBtn");

let lastMessageCount = 0;

// Format message HTML
function renderMessage(msg) {
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

    return div;
}

// Fetch and display messages
async function fetchMessages() {
    try {
        const response = await fetch(`${API_URL}/chat/history?limit=50`);
        const data = await response.json();

        if (!Array.isArray(data)) return;

        // Only re-render if new messages exist
        if (data.length !== lastMessageCount) {
            messagesDiv.innerHTML = "";
            data.forEach(msg => {
                messagesDiv.appendChild(renderMessage(msg));
            });

            // Auto-scroll to bottom
            messagesDiv.scrollTop = messagesDiv.scrollHeight;

            lastMessageCount = data.length;
        }
    } catch (err) {
        console.error("Error fetching messages:", err);
    }
}

// Send message
async function sendMessage() {
    const username = usernameInput.value.trim();
    const content = messageInput.value.trim();

    if (!username || !content) return;

    const payload = {
        username: username,
        content: content
    };

    try {
        await fetch(`${API_URL}/chat/send`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });

        messageInput.value = "";
        await fetchMessages(); // Refresh instantly
    } catch (err) {
        console.error("Error sending message:", err);
    }
}

// Event listeners
sendButton.addEventListener("click", sendMessage);

messageInput.addEventListener("keypress", (e) => {
    if (e.key === "Enter") {
        sendMessage();
    }
});

// Poll for updates every 2 seconds
setInterval(fetchMessages, 2000);

// Initial load
fetchMessages();
