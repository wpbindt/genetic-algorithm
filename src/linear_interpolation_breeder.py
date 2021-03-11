from dataclasses import dataclass
import random
from typing import List, Tuple

from .breeder import Breeder


@dataclass
class LinearInterpolationBreeder(Breeder[float]):
    crossover_rate: float

    def breed(self, population: List[float]) -> List[float]:
        new_population = []

        while len(new_population) < len(population):
            parents = tuple(random.sample(population, 2))
            new_population.extend(self._crossover(parents))

        return new_population

    def _crossover(
        self,
        parents: Tuple[float, float]
    ) -> Tuple[float, float]:
        if random.random() > self.crossover_rate:
            return parents

        interpolation = random.random()
        return (
            interpolation * parents[0] + (1 - interpolation) * parents[1],
            interpolation * parents[1] + (1 - interpolation) * parents[0]
        )
