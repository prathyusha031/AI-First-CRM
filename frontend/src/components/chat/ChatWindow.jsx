import { useSelector } from "react-redux";

function ChatWindow() {
  const { messages } = useSelector((state) => state.chat);

  return (
    <div className="chat-window">
      {messages.map((message) => (
        <div
          key={message.id}
          className={`message ${message.role === "user" ? "user" : ""}`}
        >
          <div className="avatar">
            {message.role === "assistant" ? "🤖" : "👤"}
          </div>

          <div className="bubble">
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