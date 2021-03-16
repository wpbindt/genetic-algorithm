from typing import List, Protocol

from .candidate_type import Candidate


class Mutator(Protocol[Candidate]):
    def mutate(self, population: List[Candidate]) -> List[Candidate]:
        ...
