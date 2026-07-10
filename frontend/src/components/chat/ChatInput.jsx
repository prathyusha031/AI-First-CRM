import { useState } from "react";
import { useDispatch, useSelector } from "react-redux";

import { addMessage } from "../../redux/slices/chatSlice";
import {
  setInteraction,
  setLoading,
  setError,
} from "../../redux/slices/interactionSlice";

import { logInteraction } from "../../services/interactionService";

function ChatInput() {
  const dispatch = useDispatch();

  const loading = useSelector(
  (state) => state.interaction.loading
);

  const [message, setMessage] = useState("");

  const handleSubmit = async () => {
  console.log("Button clicked");

  const text = message.trim();

  if (!text) {
    console.log("Message empty");
    return;
  }

  console.log("Sending:", text);

  dispatch(
    addMessage({
      id: Date.now(),
      role: "user",
      content: text,
    })
  );

  dispatch(setLoading(true));

  dispatch(
  addMessage({
    id: Date.now() + 100,
    role: "assistant",
    content: "Analyzing interaction...",
  })
);

  try {
    console.log("Calling backend...");

    const data = await logInteraction(text);

    console.log("========== BACKEND ==========");
    console.log(JSON.stringify(data, null, 2));
    console.log("=============================");

    dispatch(setInteraction(data));

   dispatch(
  addMessage({
    id: Date.now() + 1,
    role: "assistant",
    content:
      "I've analyzed your interaction, extracted the CRM details, and automatically updated the interaction form.",
  })
);

    setMessage("");

  } catch (err) {
    console.error("Backend Error:", err);

    dispatch(setError("Failed to contact backend."));

    dispatch(
      addMessage({
        id: Date.now() + 1,
        role: "assistant",
        content:
  "Sorry, I couldn't process your request. Please try again.",
      })
    );
  }
};
  return (
    <div className="chat-input">
      <textarea
        rows={3}
        placeholder="Example:
Met Dr. Sharma today at 11 AM. Discussed Product X, shared one brochure and two samples. Doctor was interested and requested follow-up next Tuesday."
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />

      <button
  onClick={handleSubmit}
  disabled={loading}
>
  {loading ? "Thinking..." : "Send"}
</button>
    </div>
  );
}

export default ChatInput;