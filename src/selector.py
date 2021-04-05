from typing import Callable, Protocol

from .candidate_type import Candidate


class Selector(Protocol[Candidate]):
    def select(
        self,
        population: list[Candidate],
        fitness: Callable[[Candidate], float]
    ) -> list[Candidate]:
        ...
