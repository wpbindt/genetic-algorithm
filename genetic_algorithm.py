from dataclasses import dataclass
from itertools import accumulate, repeat
from typing import Callable, Generic, TypeVar

from breeder import Breeder
from mutator import Mutator
from selector import Selector

T = TypeVar('PopulationMember')


@dataclass
class GeneticAlgorithm(Generic[T]):
    selector: Selector[T]
    breeder: Breeder[T]
    mutator: Mutator[T]
    fitness: Callable[[T], float]

    def _run_once(self, population):
        selected = self.selector.select(
            population,
            self.fitness
        )
        bred = self.breeder.breed(selected)
        return self.mutator.mutate(bred, self.fitness)

    def run(self, population):
        yield from accumulate(
            repeat(population),
            lambda x, y: self._run_once(x)
        )
