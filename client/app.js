// client/app.js

/**
 * TrojanChat Frontend Logic
 * -------------------------
 * - Handles authentication check (JWT in localStorage)
 * - Connects to Socket.io server with token
 * - Joins selected room and loads history
 * - Sends new messages and displays incoming messages
 */

document.addEventListener('DOMContentLoaded', () => {
  // Check token; if missing, redirect to login
  const token = localStorage.getItem('token');
  const username = localStorage.getItem('username');
  if (!token || !username) {
    window.location.href = '/login.html';
    return;
  }

  // Connect to Socket.io with JWT
  const socket = io('http://localhost:5000', {
    auth: {
      token
    }
  });

  const roomSelect = document.getElementById('room');
  const joinRoomBtn = document.getElementById('joinRoomBtn');
  const messagesList = document.getElementById('messages');
  const messageForm = document.getElementById('message-form');
  const messageInput = document.getElementById('message-input');
  const logoutBtn = document.getElementById('logoutBtn');

  let currentRoom = null;

  // Logout logic
  logoutBtn.addEventListener('click', () => {
    localStorage.removeItem('token');
    localStorage.removeItem('username');
    window.location.href = '/login.html';
  });

  // Join room and request history
  joinRoomBtn.addEventListener('click', () => {
    const selectedRoom = roomSelect.value;
    if (currentRoom) {
      socket.emit('leaveRoom', { room: currentRoom });
    }
    currentRoom = selectedRoom;
    messagesList.innerHTML = ''; // Clear previous messages
    socket.emit('joinRoom', { room: currentRoom });
  });

  // Render a single message in the chat window
  function renderMessage({ username: sender, text, timestamp }) {
    const li = document.createElement('li');
    li.textContent = `[${new Date(timestamp).toLocaleTimeString()}] ${sender}: ${text}`;
    if (sender === username) {
      li.class
