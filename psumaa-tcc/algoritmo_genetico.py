import random
import problem
import busca_local

# ------------------ Funções de suporte ------------------

def calculate_fitness(ind, numJobs, dataJobs, dataSetup):
    return problem.calculateCost(ind, numJobs, dataJobs, dataSetup)

def tournament_selection(population, fitness, k=3):
    selected = random.sample(list(zip(population, fitness)), k)
    return min(selected, key=lambda x: x[1])[0]

def order_crossover(p1, p2):
    size = len(p1)
    a, b = sorted(random.sample(range(size), 2))
    child = [None] * size
    child[a:b] = p1[a:b]

    p2_idx = b
    child_idx = b
    while None in child:
        if p2[p2_idx % size] not in child:
            child[child_idx % size] = p2[p2_idx % size]
            child_idx += 1
        p2_idx += 1

    return child

def mutate_swap(ind):
    a, b = random.sample(range(len(ind)), 2)
    ind[a], ind[b] = ind[b], ind[a]

# ------------------ AG com Local Search + Diversidade ------------------

def genetic_algorithm(numJobs, dataJobs, dataSetup, bestValue, pop_size=50, generations=100, mutation_rate=0.1):
    # População inicial aleatória
    population = [random.sample(range(1, numJobs + 1), numJobs) for _ in range(pop_size)]

    best_ind = None
    best_cost = float('inf')
    stagnant = 0  # contador de gerações sem melhoria

    for gen in range(generations):
        fitness = [calculate_fitness(ind, numJobs, dataJobs, dataSetup) for ind in population]

        # Atualiza melhor solução
        min_idx = fitness.index(min(fitness))
        if fitness[min_idx] < best_cost:
            best_cost = fitness[min_idx]
            best_ind = population[min_idx][:]
            stagnant = 0
        else:
            stagnant += 1

        # Verifica convergência e aplica diversidade
        if stagnant >= 10:
            for i in range(int(0.3 * pop_size)):
                population[i] = random.sample(range(1, numJobs + 1), numJobs)
            stagnant = 0

        # Nova geração
        new_population = []
        while len(new_population) < pop_size:
            parent1 = tournament_selection(population, fitness)
            parent2 = tournament_selection(population, fitness)
            child = order_crossover(parent1, parent2)

            if random.random() < mutation_rate:
                mutate_swap(child)

            # Aplica busca local nos 5 melhores filhos
            child, _ = busca_local.local_search(child, numJobs, dataJobs, dataSetup)

            new_population.append(child)

        population = new_population

    gap = problem.gap(best_cost, bestValue)
    return best_ind, best_cost, gap

