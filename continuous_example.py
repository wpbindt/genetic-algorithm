import random
from statistics import mean

from src.continuous_genetic_algorithm import ContinuousGA


def to_maximize(x: float) -> float:
    return 4 - x ** 2


lower_bound = -5
upper_bound = 5

ga = ContinuousGA(
    fitness=to_maximize,
    lower_bound=lower_bound,
    upper_bound=upper_bound,
    crossover_rate=0.1,
    mutation_rate=0.001
)

population_size = 500
population = [
    random.uniform(lower_bound, upper_bound)
    for _ in range(population_size)
]

score = mean(to_maximize(individual) for individual in population)
print(f'Average score before genetic algorithm: {score}')

evolution = ga.run(population)
generations = 500
for _ in range(generations):
    generation = next(evolution)

final_score = mean(to_maximize(individual) for individual in generation)
print(f'Average score after genetic algorithm: {final_score}')
