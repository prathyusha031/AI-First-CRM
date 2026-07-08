import "./InteractionForm.css";

function InteractionForm() {
  return (
    <>
      <div className="panel-title">
        <h2>Log HCP Interaction</h2>
      </div>

      <div className="interaction-form">

        {/* Row 1 */}

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
              <option>Conference</option>
            </select>
          </div>
        </div>

        {/* Row 2 */}

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

      </div>
    </>
  );
}

export default InteractionForm;