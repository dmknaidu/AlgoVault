import { useEffect, useMemo, useState } from "react";
import {
  getAlgorithms,
  getHealth,
  getSearchComparison,
  type Algorithm,
  type SearchComparisonResponse,
} from "./services/api";
import "./App.css";


function App() {
  const [backendStatus, setBackendStatus] = useState("Checking...");
  const [algorithms, setAlgorithms] = useState<Algorithm[]>([]);

  const [algorithmA, setAlgorithmA] = useState("linear_search");
  const [algorithmB, setAlgorithmB] = useState("binary_search");

  const [comparison, setComparison] =
    useState<SearchComparisonResponse | null>(null);

  const [loading, setLoading] = useState(false);
  const [loadingAlgorithms, setLoadingAlgorithms] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    getHealth()
      .then(() => {
        setBackendStatus("Connected");
      })
      .catch(() => {
        setBackendStatus("Disconnected");
      });

    getAlgorithms()
      .then((data) => {
        setAlgorithms(data.algorithms);
      })
      .catch(() => {
        setError("Unable to load algorithms.");
      })
      .finally(() => {
        setLoadingAlgorithms(false);
      });
  }, []);

  const selectedAlgorithmA = useMemo(
    () => algorithms.find((algorithm) => algorithm.id === algorithmA),
    [algorithms, algorithmA],
  );

  const selectedAlgorithmB = useMemo(
    () => algorithms.find((algorithm) => algorithm.id === algorithmB),
    [algorithms, algorithmB],
  );

  async function handleCompare() {
    if (algorithmA === algorithmB) {
      setError("Please select two different algorithms.");
      return;
    }

    setLoading(true);
    setError("");

    try {
      const data = await getSearchComparison(
        algorithmA,
        algorithmB,
      );

      setComparison(data);
    } catch {
      setError(
        "No benchmark data is available for this algorithm combination.",
      );
      setComparison(null);
    } finally {
      setLoading(false);
    }
  }

  const maximumSpeedup = comparison
    ? Math.max(
        ...comparison.comparisons.map((item) => item.speedup),
      )
    : null;

  return (
    <div className="app-shell">
      <aside className="sidebar">
        <div className="brand">
          <div className="brand-mark">A</div>

          <div>
            <h1>AlgoVault</h1>
            <span>DSA Intelligence Engine</span>
          </div>
        </div>

        <nav className="navigation">
          <button className="nav-item active">
            <span>⌂</span>
            Overview
          </button>

          <button className="nav-item">
            <span>◇</span>
            Algorithms
          </button>

          <button className="nav-item">
            <span>▣</span>
            Data Structures
          </button>

          <button className="nav-item">
            <span>◈</span>
            Benchmarks
          </button>

          <button className="nav-item">
            <span>⌁</span>
            Visualizer
          </button>

          <button className="nav-item">
            <span>?</span>
            Problem Lab
          </button>

          <button className="nav-item">
            <span>✦</span>
            AI Mentor
          </button>
        </nav>

        <div className="sidebar-footer">
          <div className="system-indicator">
            <span />
            <div>
              <strong>System Online</strong>
              <small>API connected</small>
            </div>
          </div>
        </div>
      </aside>

      <div className="main-area">
        <header className="topbar">
          <div>
            <span className="eyebrow">ALGORITHM INTELLIGENCE</span>
            <h2>Benchmark Workspace</h2>
          </div>

          <div className="connection-status">
            <span />
            {backendStatus}
          </div>
        </header>

        <main className="dashboard">
          <section className="hero-section">
            <div>
              <span className="section-label">PERFORMANCE LAB</span>

              <h3>
                Understand algorithms
                <br />
                through <em>evidence.</em>
              </h3>

              <p>
                Compare implementations, observe scaling behavior,
                and connect theoretical complexity with real
                execution.
              </p>
            </div>
          </section>

          <section className="comparison-panel">
            <div className="panel-heading">
              <div>
                <span className="section-label">EXPERIMENT</span>
                <h3>Algorithm Comparison</h3>
              </div>

              <span className="experiment-badge">
                {comparison
                  ? `${comparison.count} data points`
                  : "Ready"}
              </span>
            </div>

            <div className="algorithm-selectors">
              <div className="algorithm-card">
                <span className="card-label">ALGORITHM A</span>

                <select
                  value={algorithmA}
                  onChange={(event) =>
                    setAlgorithmA(event.target.value)
                  }
                  disabled={loadingAlgorithms}
                >
                  {algorithms.map((algorithm) => (
                    <option
                      key={algorithm.id}
                      value={algorithm.id}
                    >
                      {algorithm.name}
                    </option>
                  ))}
                </select>

                {selectedAlgorithmA && (
                  <div className="algorithm-meta">
                    <strong>
                      {selectedAlgorithmA.time_complexity}
                    </strong>

                    <span>
                      Space {selectedAlgorithmA.space_complexity}
                    </span>
                  </div>
                )}

                {selectedAlgorithmA && (
                  <p>{selectedAlgorithmA.description}</p>
                )}
              </div>

              <div className="versus">
                <span>VS</span>
              </div>

              <div className="algorithm-card">
                <span className="card-label">ALGORITHM B</span>

                <select
                  value={algorithmB}
                  onChange={(event) =>
                    setAlgorithmB(event.target.value)
                  }
                  disabled={loadingAlgorithms}
                >
                  {algorithms.map((algorithm) => (
                    <option
                      key={algorithm.id}
                      value={algorithm.id}
                    >
                      {algorithm.name}
                    </option>
                  ))}
                </select>

                {selectedAlgorithmB && (
                  <div className="algorithm-meta">
                    <strong>
                      {selectedAlgorithmB.time_complexity}
                    </strong>

                    <span>
                      Space {selectedAlgorithmB.space_complexity}
                    </span>
                  </div>
                )}

                {selectedAlgorithmB && (
                  <p>{selectedAlgorithmB.description}</p>
                )}
              </div>
            </div>

            <div className="compare-action">
              <button
                onClick={handleCompare}
                disabled={loading || loadingAlgorithms}
              >
                {loading ? "Running Experiment..." : "Run Comparison"}
              </button>
            </div>

            {error && (
              <div className="error-message">
                {error}
              </div>
            )}
          </section>

          {comparison && (
            <>
              <section className="metrics-grid">
                <div className="metric-card featured">
                  <span>PEAK SPEEDUP</span>

                  <strong>
                    {maximumSpeedup?.toFixed(2)}×
                  </strong>

                  <small>
                    Observed at input size{" "}
                    {comparison.comparisons.at(-1)?.input_size.toLocaleString()}
                  </small>
                </div>

                <div className="metric-card">
                  <span>{comparison.algorithm_a}</span>

                  <strong>
                    {selectedAlgorithmA?.time_complexity}
                  </strong>

                  <small>Time complexity</small>
                </div>

                <div className="metric-card">
                  <span>{comparison.algorithm_b}</span>

                  <strong>
                    {selectedAlgorithmB?.time_complexity}
                  </strong>

                  <small>Time complexity</small>
                </div>
              </section>

              <section className="panel">
                <div className="panel-heading">
                  <div>
                    <span className="section-label">MEASUREMENTS</span>
                    <h3>Benchmark Results</h3>
                  </div>
                </div>

                <div className="table-container">
                  <table>
                    <thead>
                      <tr>
                        <th>Input Size</th>
                        <th>{comparison.algorithm_a}</th>
                        <th>{comparison.algorithm_b}</th>
                        <th>Speedup</th>
                      </tr>
                    </thead>

                    <tbody>
                      {comparison.comparisons.map((item) => (
                        <tr key={item.input_size}>
                          <td>
                            {item.input_size.toLocaleString()}
                          </td>

                          <td>
                            {(
                              item.algorithm_a_time * 1000
                            ).toFixed(6)}{" "}
                            ms
                          </td>

                          <td>
                            {(
                              item.algorithm_b_time * 1000
                            ).toFixed(6)}{" "}
                            ms
                          </td>

                          <td>
                            <strong>
                              {item.speedup.toFixed(2)}×
                            </strong>
                          </td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              </section>
            </>
          )}
        </main>
      </div>
    </div>
  );
}

export default App;