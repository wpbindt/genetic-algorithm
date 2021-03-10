from abc import ABC, abstractmethod
from typing import Generic

from .candidate_type import Candidate


class Selector(ABC, Generic[Candidate]):
    @abstractmethod
    def select(self, population, fitness):
        ...
