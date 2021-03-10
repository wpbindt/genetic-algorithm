from unittest.mock import patch

from src.bit_string_mutator import BitStringMutator


@patch('random.random')
def test_bit_string_mutator(random_mock):
    mutation_rate = 0.01
    mutator = BitStringMutator(mutation_rate)
    population = [
        [True, False, True],
        [True, True, True],
        [False, False, False]
    ]
    random_mock.return_value = 2 * mutation_rate
    non_mutants = mutator.mutate(population)
    assert non_mutants == population

    random_mock.return_value = 0

    mutants = mutator.mutate(population)
    expected = [
        [not bit for bit in individual]
        for individual in population
    ]
    assert mutants == expected
