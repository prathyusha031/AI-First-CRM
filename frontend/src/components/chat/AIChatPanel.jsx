import "./AIChatPanel.css";

import ChatWindow from "./ChatWindow";
import ChatInput from "./ChatInput";

function AIChatPanel() {
  return (
    <>
      <div className="panel-title">
        <h2>🤖 AI Assistant</h2>
        <p>Log interaction details via chat</p>
      </div>

      <div className="chat-container">
        <ChatWindow />
      </div>

      <div className="chat-footer">
        <ChatInput />
      </div>
    </>
  );
}

export default AIChatPanel;