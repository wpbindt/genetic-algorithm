from abc import ABC, abstractmethod
from typing import Generic

from genetic_algorithm import T


class Breeder(ABC, Generic[T]):
    @abstractmethod
    def breed(self, population):
        ...
