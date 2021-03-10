from dataclasses import dataclass
from itertools import accumulate, repeat

from breeder import Breeder
from mutator import Mutator
from selector import Selector


@dataclass
class GeneticAlgorithm:
    selector: Selector
    breeder: Breeder
    mutator: Mutator

    def _run_once(self, population):
        return self.mutator.mutate(
            self.breeder.breed(
                self.selector.select(
                    population
                )
            )
        )

    def run(self, population):
        yield from accumulate(
            repeat(population),
            lambda x, y: self._run_once(x)
        )
