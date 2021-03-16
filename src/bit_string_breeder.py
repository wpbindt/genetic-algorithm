from dataclasses import dataclass
import random
from typing import List, Tuple

BitStringType = List[bool]


@dataclass
class BitStringBreeder:
    crossover_rate: float

    def breed(self, population: List[BitStringType]) -> List[BitStringType]:
        new_population: List[BitStringType] = []
        while len(new_population) < len(population):
            parent1, parent2 = random.sample(population, 2)
            new_population.extend(self._crossover(parent1, parent2))

        return new_population

    def _crossover(
        self,
        parent1: BitStringType,
        parent2: BitStringType
    ) -> Tuple[BitStringType, BitStringType]:
        if random.random() >= self.crossover_rate:
            return parent1, parent2

        crossover_point = random.randrange(len(parent1))
        return (
            parent1[:crossover_point] + parent2[crossover_point:],
            parent2[:crossover_point] + parent1[crossover_point:]
        )
