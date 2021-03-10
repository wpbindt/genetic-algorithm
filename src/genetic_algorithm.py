from dataclasses import dataclass
from itertools import accumulate, repeat
from typing import Callable, Generator, Generic, List

from .breeder import Breeder
from .candidate_type import Candidate
from .mutator import Mutator
from .selector import Selector


@dataclass
class GeneticAlgorithm(Generic[Candidate]):
    selector: Selector[Candidate]
    breeder: Breeder[Candidate]
    mutator: Mutator[Candidate]
    fitness: Callable[[Candidate], float]

    def _run_once(self, population: List[Candidate]) -> List[Candidate]:
        selected = self.selector.select(
            population,
            self.fitness
        )
        bred = self.breeder.breed(selected)
        return self.mutator.mutate(bred)

    def run(
        self,
        population: List[Candidate]
    ) -> Generator[List[Candidate], None, None]:
        yield from accumulate(
            repeat(population),
            lambda x, y: self._run_once(x)
        )
