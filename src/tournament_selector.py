from random import sample
from typing import Callable, List

from .candidate_type import Candidate


class TournamentSelector:
    def select(
        self,
        population: List[Candidate],
        fitness: Callable[[Candidate], float]
    ) -> List[Candidate]:
        if len(population) <= 1:
            return population

        new_population: List[Candidate] = []
        while len(new_population) < len(population):
            new_member = max(
                sample(population, 2),
                key=fitness
            )
            new_population.append(new_member)
        return new_population
