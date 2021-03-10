from abc import ABC, abstractmethod


class Breeder(ABC):
    @abstractmethod
    def breed(self, population):
        ...
