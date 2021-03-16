from typing import List, Protocol

from .candidate_type import Candidate


class Breeder(Protocol[Candidate]):
    def breed(self, population: List[Candidate]) -> List[Candidate]:
        ...
