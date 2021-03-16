from typing import Callable, List, Protocol

from .candidate_type import Candidate


class Selector(Protocol[Candidate]):
    def select(
        self,
        population: List[Candidate],
        fitness: Callable[[Candidate], float]
    ) -> List[Candidate]:
        ...
