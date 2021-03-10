from typing import Callable, List

from .bit_string_breeder import BitStringBreeder
from .bit_string_mutator import BitStringMutator
from .genetic_algorithm import GeneticAlgorithm
from .tournament_selector import TournamentSelector

BitStringType = List[bool]


class KnapSackGA(GeneticAlgorithm[BitStringType]):
    def __init__(
        self,
        crossover_rate: float,
        mutation_rate: float,
        weights: List[float],
        values: List[float],
        max_weight: float
    ) -> None:
        super().__init__(
            selector=TournamentSelector(),
            breeder=BitStringBreeder(crossover_rate),
            mutator=BitStringMutator(mutation_rate),
            fitness=KnapSackGA._build_fitness_function(
                weights=weights,
                values=values,
                max_weight=max_weight
            )
        )

    @staticmethod
    def _build_fitness_function(
        weights: List[float],
        values: List[float],
        max_weight: float
    ) -> Callable[[BitStringType], float]:
        def knapsack_value(individual: BitStringType) -> float:
            weight = sum(
                bit * weight
                for bit, weight in zip(individual, weights)
            )
            if weight > max_weight:
                return 0

            return sum(
                bit * value
                for bit, value in zip(individual, values)
            )

        return knapsack_value
