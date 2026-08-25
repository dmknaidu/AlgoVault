from algorithms.implementations.array_access import array_access
from algorithms.implementations.binary_search import binary_search
from algorithms.implementations.linear_search import linear_search
from algorithms.implementations.pair_generation import generate_pairs
from algorithms.models import Algorithm
from algorithms.registry import AlgorithmRegistry


registry = AlgorithmRegistry()


registry.register(
    Algorithm(
        id="array_access",
        name="Array Access",
        category="Array",
        description="Accesses an array element directly using its index.",
        time_complexity="O(1)",
        space_complexity="O(1)",
        implementation=array_access,
    )
)


registry.register(
    Algorithm(
        id="linear_search",
        name="Linear Search",
        category="Searching",
        description="Searches an iterable sequentially for a target value.",
        time_complexity="O(n)",
        space_complexity="O(1)",
        implementation=linear_search,
    )
)


registry.register(
    Algorithm(
        id="binary_search",
        name="Binary Search",
        category="Searching",
        description="Searches a sorted list by repeatedly dividing the search space in half.",
        time_complexity="O(log n)",
        space_complexity="O(1)",
        implementation=binary_search,
    )
)


registry.register(
    Algorithm(
        id="pair_generation",
        name="Pair Generation",
        category="Array",
        description="Generates every possible ordered pair from an input list.",
        time_complexity="O(n²)",
        space_complexity="O(n²)",
        implementation=generate_pairs,
    )
)