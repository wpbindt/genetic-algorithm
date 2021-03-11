from unittest.mock import patch

from src.random_mutator import RandomMutator


@patch('random.random')
def test_random_mutator_no_mutation(mock_random):
    mutator = RandomMutator(
        mutation_rate=0.1,
        upper_bound=10,
        lower_bound=0
    )
    population = [2, 9, 3]
    mock_random.return_value = 1

    mutants = mutator.mutate(population)
    assert mutants == population

@patch('random.uniform')
@patch('random.random')
def test_random_mutator_mutation(mock_random, mock_uniform):
    mutator = RandomMutator(
        mutation_rate=0.1,
        upper_bound=10,
        lower_bound=0
    )
    population = [2, 9, 3]
    mock_random.side_effect = [0, 1, 0]
    mock_uniform.side_effect = [1, 2]

    mutants = mutator.mutate(population)
    assert mutants == [1, 9, 2]
