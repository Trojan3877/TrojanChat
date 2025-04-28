const chatForm = document.getElementById('chat-form');
const chatMessages = document.getElementById('chat-messages');

// Listen for form submit
chatForm.addEventListener('submit', (e) => {
  e.preventDefault();

  // Get message text
  const msg = e.target.elements.msg.value;

  // Add message to DOM
  outputMessage(msg);

  // Scroll down
  chatMessages.scrollTop = chatMessages.scrollHeight;

  // Clear input
  e.target.elements.msg.value = '';
  e.target.elements.msg.focus();
});

// Output message to DOM
function outputMessage(message) {
  const div = document.createElement('div');
  div.classList.add('message');
  div.innerHTML = `<p>${message}</p>`;
  chatMessages.appendChild(div);
}
