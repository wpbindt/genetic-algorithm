from dataclasses import dataclass
import random

BitStringType = list[bool]


@dataclass
class BitStringMutator:
    mutation_rate: float

    def mutate(
        self,
        population: list[BitStringType]
    ) -> list[BitStringType]:
        return [
            self._mutate_individual(individual)
            for individual in population
        ]

    def _mutate_individual(self, individual: BitStringType) -> BitStringType:
        return [
            bit if random.random() > self.mutation_rate else not bit
            for bit in individual
        ]
