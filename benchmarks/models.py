from dataclasses import dataclass


@dataclass(frozen=True)
class BenchmarkResult:
    algorithm_id: str
    input_size: int
    runs: int
    min_time: float
    max_time: float
    mean_time: float
    median_time: float
    environment: str

@dataclass(frozen=True)
class BenchmarkComparison:
    input_size: int
    algorithm_a: str
    algorithm_b: str
    algorithm_a_time: float
    algorithm_b_time: float
    speedup: float