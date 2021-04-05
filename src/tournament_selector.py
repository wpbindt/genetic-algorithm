from random import sample
from typing import Callable

from .candidate_type import Candidate


class TournamentSelector:
    def select(
        self,
        population: list[Candidate],
        fitness: Callable[[Candidate], float]
    ) -> list[Candidate]:
        if len(population) <= 1:
            return population

        new_population: list[Candidate] = []
        while len(new_population) < len(population):
            new_member = max(
                sample(population, 2),
                key=fitness
            )
            new_population.append(new_member)
        return new_population
