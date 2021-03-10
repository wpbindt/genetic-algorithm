from abc import ABC, abstractmethod
from typing import Generic

from .candidate_type import Candidate


class Mutator(ABC, Generic[Candidate]):
    @abstractmethod
    def mutate(self, population):
        ...
