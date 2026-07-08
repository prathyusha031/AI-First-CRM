import "./InteractionForm.css";

function InteractionForm() {
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
              placeholder="Search or select HCP..."
              disabled
            />
          </div>

          <div className="form-group">
            <label>Interaction Type</label>

            <select disabled>
              <option>Meeting</option>
              <option>Call</option>
              <option>Email</option>
            </select>
          </div>
        </div>

        <div className="form-row">
          <div className="form-group">
            <label>Date</label>
            <input type="date" disabled />
          </div>

          <div className="form-group">
            <label>Time</label>
            <input type="time" disabled />
          </div>
        </div>

        <div className="form-group">
          <label>Attendees</label>
          <input
            type="text"
            placeholder="Enter names or search..."
            disabled
          />
        </div>

        <div className="form-group">
          <label>Topics Discussed</label>

          <textarea
            rows="5"
            placeholder="Enter key discussion points..."
            disabled
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
              No materials added.
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
              No samples added.
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
              <input disabled type="radio" />
              😊 Positive
            </label>

            <label>
              <input disabled type="radio" />
              😐 Neutral
            </label>

            <label>
              <input disabled type="radio" />
              😟 Negative
            </label>

          </div>

        </div>

        <div className="form-group">
          <label>Outcomes</label>

          <textarea
            rows="4"
            placeholder="Key outcomes or agreements..."
            disabled
          />
        </div>

        <div className="form-group">
          <label>Follow-up Actions</label>

          <textarea
            rows="4"
            placeholder="Describe follow-up actions..."
            disabled
          />
        </div>

      </div>
    </>
  );
}

export default InteractionForm;