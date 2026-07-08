import "./MainLayout.css";

function MainLayout({ children }) {
  return (
    <div className="app-container">
      {children}
    </div>
  );
}

export default MainLayout;