import "../styles/homepage.css";
import Navbar from "../components/layout/Navbar";
import ChatWindow from "../components/chat/ChatWindow";

export default function HomePage() {
  return (
    <div className="home-page">

      <Navbar />

      <main className="dashboard">

        {/* LEFT */}
        <section className="card">

          <div className="card-header">
            <h2>Log HCP Interaction</h2>
          </div>

          <div className="card-body">

            <h3 className="section-title">Interaction Details</h3>

            {/* Row 1 */}
            <div className="form-grid">

              <div className="field">
                <label>HCP Name</label>
                <input
                  placeholder="Search or select HCP..."
                  disabled
                />
              </div>

              <div className="field">
                <label>Interaction Type</label>

                <select disabled>
                  <option>Meeting</option>
                </select>

              </div>

            </div>

            {/* Row 2 */}
            <div className="form-grid">

              <div className="field">
                <label>Date</label>
                <input
                  placeholder="dd-mm-yyyy"
                  disabled
                />
              </div>

              <div className="field">
                <label>Time</label>
                <input
                  placeholder="--:--"
                  disabled
                />
              </div>

            </div>

            {/* Row 3 */}
            <div className="field">
              <label>Attendees</label>
              <input
                placeholder="Enter names or search..."
                disabled
              />
            </div>

            <div className="field">
              <label>Topics Discussed</label>

              <textarea
                rows="5"
                placeholder="Enter key discussion points..."
                disabled
              />

            </div>

            <button className="voice-btn">
              🎤 Summarize from Voice Note (Requires Consent)
            </button>

            <div className="section-divider" />

            <h3 className="section-title">
              Materials Shared / Samples Distributed
            </h3>

            <div className="field">
              <label>Materials Shared</label>

              <div className="placeholder-box">
                No materials added.
              </div>

            </div>

            <div className="field">
              <label>Samples Distributed</label>

              <div className="placeholder-box">
                No samples added.
              </div>

            </div>

            <div className="section-divider" />

            <h3 className="section-title">
              Observed / Inferred HCP Sentiment
            </h3>

            <div className="sentiment-row">

              <label>
                <input type="radio" disabled />
                😊 Positive
              </label>

              <label>
                <input type="radio" disabled />
                😐 Neutral
              </label>

              <label>
                <input type="radio" disabled />
                ☹️ Negative
              </label>

            </div>

            <div className="field">
              <label>Outcomes</label>

              <textarea
                rows="4"
                placeholder="Key outcomes or agreements..."
                disabled
              />

            </div>

            <div className="field">
              <label>Follow-up Actions</label>

              <textarea
                rows="4"
                placeholder="Describe follow-up actions..."
                disabled
              />

            </div>

          </div>

        </section>

        {/* RIGHT */}
        <aside className="card">

          <div className="card-header">
            <h2>🤖 AI Assistant</h2>
            <p>Log interaction details via chat</p>
          </div>

          <div className="chat-body">

          <ChatWindow />

          </div>

          <div className="chat-footer">

            <div className="chat-input">

              <textarea
                placeholder="Describe interaction..."
              />

              <button>
                Log
              </button>

            </div>

          </div>

        </aside>

      </main>

    </div>
  );
}