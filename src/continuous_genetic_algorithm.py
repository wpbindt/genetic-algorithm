from typing import Callable

from .genetic_algorithm import GeneticAlgorithm
from .linear_interpolation_breeder import LinearInterpolationBreeder
from .random_mutator import RandomMutator
from .tournament_selector import TournamentSelector


class ContinuousGA(GeneticAlgorithm[float]):
    def __init__(
        self,
        fitness: Callable[[float], float],
        lower_bound: float,
        upper_bound: float,
        crossover_rate: float,
        mutation_rate: float
    ) -> None:
        super().__init__(
            selector=TournamentSelector(),
            breeder=LinearInterpolationBreeder(crossover_rate),
            mutator=RandomMutator(
                mutation_rate=mutation_rate,
                upper_bound=upper_bound,
                lower_bound=lower_bound
            ),
            fitness=fitness
        )
