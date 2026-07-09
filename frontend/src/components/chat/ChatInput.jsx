import { useState } from "react";
import { useDispatch } from "react-redux";
import { addMessage } from "../../redux/slices/chatSlice";

function ChatInput() {
  const dispatch = useDispatch();

  const [message, setMessage] = useState("");

  const handleSubmit = () => {
    const text = message.trim();

    if (!text) return;

    dispatch(
      addMessage({
        id: Date.now(),
        role: "user",
        content: text,
      })
    );

    setMessage("");

    // FastAPI call will be added here
  };

  return (
    <div className="chat-input">

      <textarea
        rows={2}
        placeholder="Describe your interaction with the HCP..."
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />

      <button onClick={handleSubmit}>
        Log
      </button>

    </div>
  );
}

export default ChatInput;