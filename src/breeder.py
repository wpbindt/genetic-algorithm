from abc import ABC, abstractmethod
from typing import Generic

from .candidate_type import Candidate


class Breeder(ABC, Generic[Candidate]):
    @abstractmethod
    def breed(self, population):
        ...
