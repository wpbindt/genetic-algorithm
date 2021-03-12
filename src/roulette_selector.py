import random
from typing import Callable, List

from .candidate_type import Candidate
from .selector import Selector


class RouletteSelector(Selector[Candidate]):
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
