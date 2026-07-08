import "./MainLayout.css";

function MainLayout({ children }) {
  return (
    <div className="app">
      <header className="navbar">
        <div className="logo">
          AI First CRM
        </div>

        <div className="user-info">
          Healthcare CRM
        </div>
      </header>

      <main className="main-wrapper">
        {children}
      </main>
    </div>
  );
}

export default MainLayout;