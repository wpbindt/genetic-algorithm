from typing import Protocol

from .candidate_type import Candidate


class Breeder(Protocol[Candidate]):
    def breed(self, population: list[Candidate]) -> list[Candidate]:
        ...
