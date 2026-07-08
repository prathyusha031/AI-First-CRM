import "./DashboardLayout.css";

import InteractionForm from "../interaction/InteractionForm";
import AIChatPanel from "../chat/AIChatPanel";

function DashboardLayout() {
  return (
    <div className="dashboard">

      <div className="interaction-panel">
        <InteractionForm />
      </div>

      <div className="assistant-panel">
        <AIChatPanel />
      </div>

    </div>
  );
}

export default DashboardLayout;