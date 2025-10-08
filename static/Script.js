const chatBox = document.getElementById("chat-box");
const inputField = document.getElementById("userInput");

//  Backend API URL setup
const API_URL = (location.hostname === "localhost" || location.hostname === "127.0.0.1")
  ? "http://127.0.0.1:5000/get"
  : "/get";

// Add message to chat box
function appendMessage(text, type) {
  const msg = document.createElement("div");
  msg.className = `msg ${type}`;
  msg.innerHTML = text;
  chatBox.appendChild(msg);
  chatBox.scrollTop = chatBox.scrollHeight;
}

// Typing indicator
function toggleTyping(show = true) {
  let typing = document.getElementById("typing");
  if (show) {
    if (!typing) {
      typing = document.createElement("div");
      typing.id = "typing";
      typing.className = "msg bot";
      typing.innerHTML = `<span class="typing"></span><span class="typing"></span><span class="typing"></span>`;
      chatBox.appendChild(typing);
    }
  } else if (typing) typing.remove();
}

// Send message to Flask backend
async function sendMessage() {
  const userText = inputField.value.trim();
  if (!userText) return;

  appendMessage(userText, "user");
  inputField.value = "";
  toggleTyping(true);

  try {
    const res = await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: userText })
    });
    const data = await res.json();

    setTimeout(() => {
      toggleTyping(false);
      appendMessage(data.reply || "⚠️ No reply received.", "bot");
    }, 1000);
  } catch {
    toggleTyping(false);
    appendMessage("⚠️ Connection error. Please try again.", "bot");
  }
}

// Welcome message with typing effect
window.onload = () => {
  const text = "👋 Welcome to Government Polytechnic Patna-07 Campus Chatbot! 🎓 You Can Ask me any Information about college.";
  typeWriterEffect(text);
};

// Typing animation for welcome message
function typeWriterEffect(text) {
  const msg = document.createElement("div");
  msg.className = "msg bot";
  chatBox.appendChild(msg);

  let i = 0;
  (function typing() {
    if (i < text.length) {
      msg.innerHTML += text.charAt(i++);
      setTimeout(typing, 50);
    }
  })();
}
