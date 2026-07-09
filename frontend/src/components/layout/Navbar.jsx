import "./Navbar.css";

export default function Navbar() {
  return (
    <header className="navbar">
      <div className="navbar-left">
        <div className="logo">
          AI
        </div>

        <div>
          <h1>AI First CRM</h1>
          <span>Healthcare Professional Interaction Assistant</span>
        </div>
      </div>

      <div className="navbar-right">
        <span className="badge">
          Healthcare CRM
        </span>
      </div>
    </header>
  );
}