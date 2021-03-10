from unittest.mock import Mock

from src.genetic_algorithm import GeneticAlgorithm


def test_genetic_algorithm():
    mock = Mock()
    genetic_algorithm = GeneticAlgorithm(
        selector=mock,
        breeder=mock,
        mutator=mock,
        fitness=mock
    )

    output = genetic_algorithm.run(['dummy population'])
    for iteration in range(10):
        next(output)
        assert mock.select.call_count == iteration
        assert mock.breed.call_count == iteration
        assert mock.mutate.call_count == iteration
