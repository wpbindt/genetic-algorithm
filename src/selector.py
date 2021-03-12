from abc import ABC, abstractmethod
from typing import Callable, Generic, List

from .candidate_type import Candidate


class Selector(ABC, Generic[Candidate]):
    @abstractmethod
    def select(
        self,
        population: List[Candidate],
        fitness: Callable[[Candidate], float]
    ) -> List[Candidate]:
        ...
