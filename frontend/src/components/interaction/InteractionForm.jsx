import { useSelector } from "react-redux";
import "./InteractionForm.css";

function InteractionForm() {
  const interaction = useSelector((state) => state.interaction);

  return (
    <>
      <div className="panel-title">
        <h2>Log HCP Interaction</h2>
      </div>

      <div className="interaction-form">
        <h3 className="section-title">Interaction Details</h3>

        <div className="form-row">
          <div className="form-group">
            <label>HCP Name</label>

            <input
              type="text"
              value={interaction.hcp_name || ""}
              placeholder="Search or select HCP..."
              disabled
              readOnly
            />
          </div>

          <div className="form-group">
            <label>Interaction Type</label>

            <select
              value={interaction.interaction_type || ""}
              disabled
            >
              <option value="">Select</option>
              <option value="Meeting">Meeting</option>
              <option value="Call">Call</option>
              <option value="Email">Email</option>
            </select>
          </div>
        </div>

        <div className="form-row">
          <div className="form-group">
            <label>Date</label>

            <input
              type="text"
              value={interaction.interaction_date || ""}
              placeholder="YYYY-MM-DD"
              disabled
              readOnly
            />
          </div>

          <div className="form-group">
            <label>Time</label>

            <input
              type="text"
              value={interaction.interaction_time || ""}
              placeholder="HH:MM"
              disabled
              readOnly
            />
          </div>
        </div>

        <div className="form-group">
          <label>Attendees</label>

          <input
            type="text"
            value={interaction.attendees || ""}
            placeholder="AI will populate attendees"
            disabled
            readOnly
          />
        </div>

        <div className="form-group">
          <label>Topics Discussed</label>

          <textarea
            rows="5"
            value={interaction.topics_discussed || ""}
            placeholder="AI will summarize discussion topics"
            disabled
            readOnly
          />
        </div>

        <button
          className="voice-button"
          disabled
        >
          🎤 Summarize from Voice Note (Requires Consent)
        </button>

        <hr className="divider" />

        <h3 className="section-title">
          Materials Shared / Samples Distributed
        </h3>

        <div className="form-group">
          <label>Materials Shared</label>

          <div className="inline-action">
            <div className="placeholder-text">
              {interaction.materials?.length
                ? interaction.materials.join(", ")
                : "No materials shared."}
            </div>

            <button disabled>
              🔍 Search/Add
            </button>
          </div>
        </div>

        <div className="form-group">
          <label>Samples Distributed</label>

          <div className="inline-action">
            <div className="placeholder-text">
              {interaction.samples?.length
                ? interaction.samples.join(", ")
                : "No samples distributed."}
            </div>

            <button disabled>
              ➕ Add Sample
            </button>
          </div>
        </div>

        <hr className="divider" />

        <div className="form-group">
          <label>Observed/Inferred HCP Sentiment</label>

          <div className="radio-row">
            <label>
              <input
                type="radio"
                checked={
                  interaction.sentiment?.toLowerCase() === "positive"
                }
                disabled
                readOnly
              />
              😊 Positive
            </label>

            <label>
              <input
                type="radio"
                checked={
                  interaction.sentiment?.toLowerCase() === "neutral"
                }
                disabled
                readOnly
              />
              😐 Neutral
            </label>

            <label>
              <input
                type="radio"
                checked={
                  interaction.sentiment?.toLowerCase() === "negative"
                }
                disabled
                readOnly
              />
              😟 Negative
            </label>
          </div>
        </div>

        <div className="form-group">
          <label>Outcomes</label>

          <textarea
            rows="4"
            value={interaction.outcomes || ""}
            placeholder="AI will summarize outcomes"
            disabled
            readOnly
          />
        </div>

        <div className="form-group">
          <label>Follow-up Actions</label>

          <textarea
            rows="4"
            value={interaction.follow_up_actions || ""}
            placeholder="AI will generate follow-up actions"
            disabled
            readOnly
          />
        </div>
      </div>
    </>
  );
}

export default InteractionForm;