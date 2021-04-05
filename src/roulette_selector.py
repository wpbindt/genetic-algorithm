import random
from typing import Callable

from .candidate_type import Candidate


class RouletteSelector:
    def select(
        self,
        population: list[Candidate],
        fitness: Callable[[Candidate], float]
    ) -> list[Candidate]:
        fitness_scores = [
            fitness(individual)
            for individual in population
        ]

        return random.choices(
            population,
            weights=fitness_scores,
            k=len(population)
        )
