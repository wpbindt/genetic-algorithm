from src.tournament_selector import TournamentSelector


def test_tournament_select():
    selector = TournamentSelector()
    assert selector.select([], lambda x: x) == []
    assert selector.select([1], lambda x: x) == [1]
    assert selector.select([1, 2], lambda x: x) == [2, 2]
    assert selector.select([1, 2, 2], lambda x: x) == [2, 2, 2]
    assert selector.select([1, 2], lambda x: -x) == [1, 1]


def test_population_size_invariant():
    selector = TournamentSelector()
    population = list(range(100))
    assert len(selector.select(population, lambda x: x)) == len(population)
