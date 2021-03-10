from abc import ABC, abstractmethod
from typing import Generic

from genetic_algorithm import T


class Mutator(ABC, Generic[T]):
    @abstractmethod
    def mutate(self, population):
        ...
