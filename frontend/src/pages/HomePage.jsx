import "../styles/homepage.css";

import Navbar from "../components/layout/Navbar";
import InteractionForm from "../components/interaction/InteractionForm";
import AIChatPanel from "../components/chat/AIChatPanel";

export default function HomePage() {
  return (
    <div className="home-page">
      <Navbar />

      <main className="dashboard">
        {/* LEFT */}
        <section className="card">
          <InteractionForm />
        </section>

        {/* RIGHT */}
        <aside className="card">
          <AIChatPanel />
        </aside>
      </main>
    </div>
  );
}