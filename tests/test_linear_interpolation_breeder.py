from unittest.mock import patch

from src.linear_interpolation_breeder import LinearInterpolationBreeder


@patch('random.random')
def test_linear_interpolation_no_breeding(random_mock):
    breeder = LinearInterpolationBreeder(0.1)
    population = [1, 3]
    random_mock.return_value = 1
    actual = breeder.breed(population)
    assert len(actual) == len(population)
    assert set(actual) == set(population)


@patch('random.random')
def test_linear_interpolation_breeding(random_mock):
    breeder = LinearInterpolationBreeder(0.1)
    individual1 = 1
    individual2 = 3
    population = [individual1, individual2]
    interpolation = 0.3
    random_mock.side_effect = [0, interpolation]
    actual = breeder.breed(population)
    assert set(actual) == {
        interpolation * individual1 + (1 - interpolation) * individual2,
        interpolation * individual2 + (1 - interpolation) * individual1
    }
