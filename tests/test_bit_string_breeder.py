from unittest.mock import patch

from src.bit_string_breeder import BitStringBreeder


@patch('random.random')
def test_bit_string_breeder_no_crossover(random_mock):
    random_mock.return_value = 1
    breeder = BitStringBreeder(0.1)
    population = [
        4 * [True],
        4 * [False]
    ]

    bred = breeder.breed(population)
    assert len(bred) == len(population)
    assert bred[0] in population
    assert bred[1] in population


@patch('random.random')
@patch('random.randint')
def test_bit_string_breeder_crossover(randint_mock, random_mock):
    random_mock.return_value = 0
    randint_mock.return_value = 2
    breeder = BitStringBreeder(0.1)
    population = [
        4 * [True],
        4 * [False]
    ]

    bred = breeder.breed(population)
    assert len(bred) == len(population)
    assert [True, True, False, False] in bred
    assert [False, False, True, True] in bred


def test_bit_string_breeder_empty():
    breeder = BitStringBreeder(0.1)
    assert breeder.breed([]) == []
