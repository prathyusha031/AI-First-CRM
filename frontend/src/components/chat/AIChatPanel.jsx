import "./AIChatPanel.css";

function AIChatPanel() {
  return (
    <>
      <div className="panel-title">
        <h2>AI Assistant</h2>
        <p>Log interaction via chat</p>
      </div>

      <div className="chat-container">
        <div className="assistant-message">
          <p>
            Log interaction details here.
          </p>

          <span>
            Example:
            <br />
            "Met Dr. Smith today, discussed Product X efficacy, shared
            brochure and sample, follow up next Tuesday."
          </span>
        </div>
      </div>

      <div className="chat-footer">
        <input
          type="text"
          placeholder="Describe interaction..."
        />

        <button>
          Log
        </button>
      </div>
    </>
  );
}

export default AIChatPanel;