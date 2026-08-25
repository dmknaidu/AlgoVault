from dataclasses import dataclass
from typing import Callable, Any


@dataclass(frozen=True)
class Algorithm:
    id: str
    name: str
    category: str
    description: str
    time_complexity: str
    space_complexity: str
    implementation: Callable[..., Any]