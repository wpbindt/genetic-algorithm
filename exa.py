import numpy

from src.knapsack_genetic_algorithm import KnapsackDefinition, KnapsackGA

problem = KnapsackDefinition(
    values=[9, 2, 0, 3, 2],
    weights=[5, 2, 1, 2, 4],
    max_weight=7
)

ga = KnapsackGA(
    mutation_rate=0.01,
    crossover_rate=0.1,
    knapsack_definition=problem
)

population_size = 200
population = numpy.random.choice(
    [True, False],
    size=(population_size, 5)
).tolist()

score = sum(
    ga.fitness(individual)
    for individual in population
)
print(f'Total population score before GA: {score}')

evolution = ga.run(population)
generations = 500
for _ in range(generations):
    generation = next(evolution)

final_score = sum(
    ga.fitness(individual)
    for individual in generation
)
print(f'Total population score after GA: {final_score}')
