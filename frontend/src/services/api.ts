const API_BASE_URL = "http://127.0.0.1:8000";

export interface BenchmarkResult {
  algorithm_id: string;
  input_size: number;
  runs: number;
  min_time: number;
  max_time: number;
  mean_time: number;
  median_time: number;
  environment: string;
}

export interface BenchmarkComparison {
  input_size: number;
  algorithm_a_time: number;
  algorithm_b_time: number;
  speedup: number;
}

export interface SearchComparisonResponse {
  algorithm_a: string;
  algorithm_b: string;
  count: number;
  comparisons: BenchmarkComparison[];
}


export async function getHealth() {
  const response = await fetch(`${API_BASE_URL}/health`);

  if (!response.ok) {
    throw new Error("Backend health check failed");
  }

  return response.json();
}


export async function getSearchComparison(
  algorithmA: string,
  algorithmB: string,
): Promise<SearchComparisonResponse> {
  const params = new URLSearchParams({
    algorithm_a: algorithmA,
    algorithm_b: algorithmB,
  });

  const response = await fetch(
    `${API_BASE_URL}/api/benchmarks/search/comparison?${params.toString()}`,
  );

  if (!response.ok) {
    throw new Error("Failed to load benchmark comparison");
  }

  return response.json();
}

export interface Algorithm {
  id: string;
  name: string;
  category: string;
  description: string;
  time_complexity: string;
  space_complexity: string;
}

export interface AlgorithmsResponse {
  count: number;
  algorithms: Algorithm[];
}

export async function getAlgorithms(): Promise<AlgorithmsResponse> {
  const response = await fetch(`${API_BASE_URL}/api/algorithms`);

  if (!response.ok) {
    throw new Error("Failed to load algorithms");
  }

  return response.json();
}