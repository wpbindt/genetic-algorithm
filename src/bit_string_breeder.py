from dataclasses import dataclass
import random
from typing import List, Tuple

from .breeder import Breeder


BitStringType = List[bool]


@dataclass
class BitStringBreeder(Breeder[BitStringType]):
    crossover_rate: float

    def breed(self, population: List[BitStringType]) -> List[BitStringType]:
        new_population = []
        while len(new_population) < len(population):
            parents = tuple(random.sample(population, 2))
            new_population.extend(self._crossover(parents))

        return new_population

    def _crossover(
        self,
        parents: Tuple[BitStringType, BitStringType]
    ) -> Tuple[BitStringType, BitStringType]:
        if random.random() >= self.crossover_rate:
            return parents

        crossover_point = random.randint(0, len(parents[0]) - 1)
        return (
            parents[0][:crossover_point] + parents[1][crossover_point:],
            parents[1][:crossover_point] + parents[0][crossover_point:]
        )
