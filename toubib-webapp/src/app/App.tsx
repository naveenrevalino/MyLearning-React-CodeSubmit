import "./App.css";
import PatientPage from "./components/PatientPage";

function App() {
  return (
    <div id="app" className="App-container">
      <div className="App-header">
        <h1 className="App-title">Toubib Full-stack</h1>
      </div>
      <PatientPage />
      <div className="App-footer">Dialogue © 2023</div>
    </div>
  );
}

export default App;
