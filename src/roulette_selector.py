import random
from typing import Callable, List

from .candidate_type import Candidate


class RouletteSelector:
    def select(
        self,
        population: List[Candidate],
        fitness: Callable[[Candidate], float]
    ) -> List[Candidate]:
        fitness_scores = [
            fitness(individual)
            for individual in population
        ]

        return random.choices(
            population,
            weights=fitness_scores,
            k=len(population)
        )
