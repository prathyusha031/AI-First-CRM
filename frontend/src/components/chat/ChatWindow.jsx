import { useSelector } from "react-redux";

function ChatWindow() {
  const { messages } = useSelector((state) => state.chat);

  return (
    <div className="chat-window">

      {/* Default AI message */}
      <div className="message assistant">

        <div className="avatar">
          🤖
        </div>

        <div className="bubble assistant-bubble">
          <strong>AI Assistant</strong>

          <p>
            Log interaction details here (e.g. "Met Dr. Sharma,
            discussed Product X, shared brochure, positive
            sentiment...") or ask for help.
          </p>
        </div>

      </div>

      {/* Conversation */}

      {messages.map((message) => (
        <div
          key={message.id}
          className={`message ${
            message.role === "user"
              ? "user"
              : "assistant"
          }`}
        >
          <div className="avatar">
            {message.role === "assistant"
              ? "🤖"
              : "👤"}
          </div>

          <div
            className={`bubble ${
              message.role === "assistant"
                ? "assistant-bubble"
                : "user-bubble"
            }`}
          >
            <strong>
              {message.role === "assistant"
                ? "AI Assistant"
                : "You"}
            </strong>

            <p>{message.content}</p>

          </div>

        </div>
      ))}

    </div>
  );
}

export default ChatWindow;