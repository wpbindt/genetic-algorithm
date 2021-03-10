from abc import ABC, abstractmethod
from typing import Generic

from genetic_algorithm import T


class Selector(ABC, Generic[T]):
    @abstractmethod
    def select(self, population, fitness):
        ...
