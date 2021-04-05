from typing import Protocol

from .candidate_type import Candidate


class Mutator(Protocol[Candidate]):
    def mutate(self, population: list[Candidate]) -> list[Candidate]:
        ...
