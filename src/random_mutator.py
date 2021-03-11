from dataclasses import dataclass
import random
from typing import List

from .mutator import Mutator


@dataclass
class RandomMutator(Mutator[float]):
    mutation_rate: float
    upper_bound: float
    lower_bound: float

    def mutate(self, population: List[float]) -> List[float]:
        return [
            self._mutate_individual(individual)
            for individual in population
        ]

    def _mutate_individual(self, individual: float) -> float:
        if random.random() > self.mutation_rate:
            return individual

        return random.uniform(self.lower_bound, self.upper_bound)
