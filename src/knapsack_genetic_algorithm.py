from __future__ import annotations
from typing import Callable, List

from .bit_string_breeder import BitStringBreeder
from .bit_string_mutator import BitStringMutator
from .genetic_algorithm import GeneticAlgorithm
from .tournament_selector import TournamentSelector

BitStringType = List[bool]


class KnapsackGA(GeneticAlgorithm[BitStringType]):
    def __init__(
        self,
        crossover_rate: float,
        mutation_rate: float,
        knapsack_definition: KnapsackDefinition
    ) -> None:
        super().__init__(
            selector=TournamentSelector(),
            breeder=BitStringBreeder(crossover_rate),
            mutator=BitStringMutator(mutation_rate),
            fitness=KnapsackGA._build_fitness_function(knapsack_definition)
        )

    @staticmethod
    def _build_fitness_function(
        knapsack_definition: KnapsackDefinition
    ) -> Callable[[BitStringType], float]:
        def knapsack_value(individual: BitStringType) -> float:
            weight = sum(
                bit * weight
                for bit, weight in zip(individual, knapsack_definition.weights)
            )
            if weight > knapsack_definition.max_weight:
                return 0

            return sum(
                bit * value
                for bit, value in zip(individual, knapsack_definition.values)
            )

        return knapsack_value


@dataclass
class KnapsackDefinition:
    weights: List[float]
    values: List[float]
    max_weight: float

