/* agent.js */
const agentTemplate = `
<div id="agent-widget">
  <button id="agent-button">
    <span>Ask Krish AI</span>
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
      <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
    </svg>
  </button>
  <div id="agent-panel">
    <div id="agent-header">
      <h3>Ask Krish AI</h3>
      <button id="agent-close">&times;</button>
    </div>
    <div id="agent-messages">
      <div class="agent-msg bot">Hi! I'm Krish's personal AI assistant. You can ask me about his projects, skills, or experience.</div>
      <div id="agent-suggestions">
        <button class="agent-sugg-btn">What did Krish build?</button>
        <button class="agent-sugg-btn">Tell me about ImpactGlobe.</button>
        <button class="agent-sugg-btn">How can I contact Krish?</button>
      </div>
    </div>
    <div id="agent-input-area">
      <input type="text" id="agent-input" placeholder="Type a message..." aria-label="Ask Krish AI" />
      <button id="agent-send">Send</button>
    </div>
  </div>
</div>
`;

document.addEventListener("DOMContentLoaded", () => {
  document.body.insertAdjacentHTML('beforeend', agentTemplate);

  const btn = document.getElementById("agent-button");
  const panel = document.getElementById("agent-panel");
  const closeBtn = document.getElementById("agent-close");
  const sendBtn = document.getElementById("agent-send");
  const input = document.getElementById("agent-input");
  const messagesDiv = document.getElementById("agent-messages");

  let conversationHistory = [];

  function togglePanel() {
    panel.classList.toggle("open");
    if (panel.classList.contains("open")) {
      input.focus();
    }
  }

  btn.addEventListener("click", togglePanel);
  closeBtn.addEventListener("click", togglePanel);

  function appendMessage(role, text) {
    const msg = document.createElement("div");
    msg.className = \`agent-msg \${role}\`;
    msg.textContent = text;
    messagesDiv.appendChild(msg);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
  }

  async function sendMessage(text) {
    if (!text.trim()) return;
    
    appendMessage("user", text);
    conversationHistory.push({ role: "user", content: text });
    input.value = "";

    // Show loading state
    const loadingId = "loading-" + Date.now();
    const loadingMsg = document.createElement("div");
    loadingMsg.id = loadingId;
    loadingMsg.className = "agent-msg bot";
    loadingMsg.innerHTML = "<i>Thinking...</i>";
    messagesDiv.appendChild(loadingMsg);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;

    try {
      const res = await fetch("/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ messages: conversationHistory })
      });

      const data = await res.json();
      document.getElementById(loadingId).remove();

      if (res.ok) {
        appendMessage("bot", data.reply);
        conversationHistory.push({ role: "assistant", content: data.reply });
      } else {
        appendMessage("bot", "Error: " + (data.error || "Failed to reach AI."));
      }
    } catch (err) {
      document.getElementById(loadingId).remove();
      appendMessage("bot", "Network error. Please try again later.");
    }
  }

  sendBtn.addEventListener("click", () => sendMessage(input.value));
  input.addEventListener("keypress", (e) => {
    if (e.key === "Enter") sendMessage(input.value);
  });

  document.querySelectorAll(".agent-sugg-btn").forEach(btn => {
    btn.addEventListener("click", (e) => {
      e.target.parentElement.remove();
      sendMessage(e.target.textContent);
    });
  });
});
