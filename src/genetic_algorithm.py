from itertools import accumulate, repeat
from typing import Callable, Generator, Generic

from .breeder import Breeder
from .candidate_type import Candidate
from .mutator import Mutator
from .selector import Selector


class GeneticAlgorithm(Generic[Candidate]):
    def __init__(
        self,
        selector: Selector[Candidate],
        breeder: Breeder[Candidate],
        mutator: Mutator[Candidate],
        fitness: Callable[[Candidate], float]
    ) -> None:
        self.selector = selector
        self.breeder = breeder
        self.mutator = mutator
        self.fitness = fitness

    def _run_once(self, population: list[Candidate]) -> list[Candidate]:
        selected = self.selector.select(
            population,
            self.fitness
        )
        bred = self.breeder.breed(selected)
        return self.mutator.mutate(bred)

    def run(
        self,
        population: list[Candidate]
    ) -> Generator[list[Candidate], None, None]:
        yield from accumulate(
            repeat(population),
            lambda x, y: self._run_once(x)
        )
