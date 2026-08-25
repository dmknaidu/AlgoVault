from algorithms.models import Algorithm


class AlgorithmRegistry:
    def __init__(self):
        self._algorithms: dict[str, Algorithm] = {}

    def register(self, algorithm: Algorithm) -> None:
        if algorithm.id in self._algorithms:
            raise ValueError(
                f"Algorithm '{algorithm.id}' is already registered."
            )

        self._algorithms[algorithm.id] = algorithm

    def get(self, algorithm_id: str) -> Algorithm:
        try:
            return self._algorithms[algorithm_id]
        except KeyError:
            raise KeyError(
                f"Algorithm '{algorithm_id}' is not registered."
            )

    def list_all(self) -> list[Algorithm]:
        return list(self._algorithms.values())

    def list_by_category(self, category: str) -> list[Algorithm]:
        return [
            algorithm
            for algorithm in self._algorithms.values()
            if algorithm.category == category
        ]