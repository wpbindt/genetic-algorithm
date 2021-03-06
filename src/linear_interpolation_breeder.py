from dataclasses import dataclass
import random


@dataclass
class LinearInterpolationBreeder:
    crossover_rate: float

    def breed(self, population: list[float]) -> list[float]:
        new_population: list[float] = []

        while len(new_population) < len(population):
            parent1, parent2 = random.sample(population, 2)
            new_population.extend(self._crossover(parent1, parent2))

        return new_population

    def _crossover(
        self,
        parent1: float,
        parent2: float
    ) -> tuple[float, float]:
        if random.random() > self.crossover_rate:
            return parent1, parent2

        interpolation = random.random()
        return (
            interpolation * parent1 + (1 - interpolation) * parent2,
            interpolation * parent2 + (1 - interpolation) * parent1
        )
