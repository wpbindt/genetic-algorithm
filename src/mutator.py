from abc import ABC, abstractmethod
from typing import Generic

from .genetic_algorithm import Candidate


class Mutator(ABC, Generic[Candidate]):
    @abstractmethod
    def mutate(self, population):
        ...
