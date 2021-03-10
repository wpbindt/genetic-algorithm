from dataclasses import dataclass
import random
from typing import List

from .mutator import Mutator


@dataclass
class BitStringMutator(Mutator[List[bool]]):
    mutation_rate: float

    def mutate(
        self,
        population: List[List[bool]]
    ) -> List[List[bool]]:
        return [
            self._mutate_individual(individual)
            for individual in population
        ]

    def _mutate_individual(self, individual: List[bool]) -> List[bool]:
        return [
            bit if random.random() > self.mutation_rate else not bit
            for bit in individual
        ]
