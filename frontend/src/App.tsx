import { useEffect, useState } from "react";
import { getHealth } from "./services/api";

function App() {
  const [backendStatus, setBackendStatus] = useState("Checking...");

  useEffect(() => {
    getHealth()
      .then(() => {
        setBackendStatus("Connected");
      })
      .catch(() => {
        setBackendStatus("Disconnected");
      });
  }, []);

  return (
    <div>
      <header>
        <h1>AlgoVault</h1>
        <p>Intelligent Algorithm & Data Structure Engine</p>
      </header>

      <main>
        <section>
          <h2>Welcome to AlgoVault</h2>

          <p>
            Learn, implement, visualize, benchmark, and practice
            data structures and algorithms.
          </p>

          <p>
            Backend Status: <strong>{backendStatus}</strong>
          </p>
        </section>

        <section>
          <h2>Modules</h2>

          <ul>
            <li>Algorithms</li>
            <li>Data Structures</li>
            <li>Visualizations</li>
            <li>Benchmarks</li>
            <li>Problem Lab</li>
            <li>AI Mentor</li>
          </ul>
        </section>
      </main>
    </div>
  );
}

export default App;