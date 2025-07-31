import problem
import random
import heuristica_construtiva
import busca_local
import busca_tabu
import algoritmo_genetico
import numpy as np

# ------------------- LEITURA DOS ARQUIVOS -------------------

sourceFile = './instances/dados/INST0801.dat'
solutionFile = './instances/saida/inst0801.sol'
numJobs, dataJobs, dataSetup, bestValue = problem.readFiles(sourceFile, solutionFile)

# ------------------- ALGORITMO GENÉTICO -------------------

print("\nAntes do Algoritmo Genético:")
solution = random.sample(range(1, numJobs + 1), numJobs)
cost = problem.calculateCost(solution, numJobs, dataJobs, dataSetup)
print("Solução Inicial:", solution)
print("Custo Inicial...:", cost)

melhor_solucao_ag, melhor_custo_ag, gap_ag = algoritmo_genetico.genetic_algorithm(numJobs, dataJobs, dataSetup, bestValue, pop_size=100, generations=300, mutation_rate=0.15)
print("\nAlgoritmo Genético (com Local Search + Diversidade):")
print("Melhor Solução:", melhor_solucao_ag)
print("Custo...:", melhor_custo_ag)
print("GAP......: %.2f%%" % gap_ag)

# ------------------- HEURÍSTICA CONSTRUTIVA -------------------

print("\nHeurística Construtiva Parcialmente Gulosa:")
solucao_heuristica = heuristica_construtiva.greedy_construction(numJobs, dataJobs, dataSetup)
custo_heuristica = problem.calculateCost(solucao_heuristica, numJobs, dataJobs, dataSetup)
gap_heuristica = problem.gap(custo_heuristica, bestValue)
print("Solução Heurística:", solucao_heuristica)
print("Custo (Heurística)...: ", custo_heuristica)
print("GAP (Heurística)....: %.2f%%" % gap_heuristica)

# ------------------- BUSCA LOCAL -------------------

print("\nBusca Local (2-opt):")
solution_local = list(range(1, numJobs + 1))
random.shuffle(solution_local)
solution_local, cost_local = busca_local.local_search(solution_local, numJobs, dataJobs, dataSetup)
gap_local = problem.gap(cost_local, bestValue)
print("Solução Local Search:", solution_local)
print("Custo (Busca Local)...: ", cost_local)
print("GAP (Busca Local)....: %.2f%%" % gap_local)

# ------------------- BUSCA TABU -------------------

print("\nBusca Tabu:")
solution_tabu = list(range(1, numJobs + 1))
random.shuffle(solution_tabu)
melhor_solucao_tabu, melhor_custo_tabu = busca_tabu.busca_tabu(solution_tabu, numJobs, dataJobs, dataSetup)
gap_tabu = problem.gap(melhor_custo_tabu, bestValue)
print("Melhor Solução Tabu:", melhor_solucao_tabu)
print("Custo (Busca Tabu)...: ", melhor_custo_tabu)
print("GAP (Busca Tabu)....: %.2f%%" % gap_tabu)

# ------------------- AG COM BUSCA TABU + ADAPTATIVA + DIVERSIDADE -------------------

def hamming_distance(seq1, seq2):
    return sum([1 for a, b in zip(seq1, seq2) if a != b])

def calculate_population_diversity(population):
    diversities = []
    for i in range(len(population)):
        for j in range(i + 1, len(population)):
            diversities.append(hamming_distance(population[i], population[j]))
    return np.mean(diversities) if diversities else 0

def genetic_algorithm_advanced(numJobs, dataJobs, dataSetup, bestValue, pop_size=100, generations=300, mutation_rate=0.15):
    population = [random.sample(range(1, numJobs + 1), numJobs) for _ in range(pop_size)]
    best_ind = None
    best_cost = float('inf')
    stagnant = 0

    for gen in range(generations):
        fitness = [problem.calculateCost(ind, numJobs, dataJobs, dataSetup) for ind in population]
        min_idx = fitness.index(min(fitness))

        if fitness[min_idx] < best_cost:
            best_cost = fitness[min_idx]
            best_ind = population[min_idx][:]
            stagnant = 0
        else:
            stagnant += 1

        diversity = calculate_population_diversity(population)
        if diversity < (numJobs * 0.3):
            for i in range(int(0.4 * pop_size)):
                population[i] = random.sample(range(1, numJobs + 1), numJobs)

        if stagnant >= 20:
            for i in range(int(0.5 * pop_size)):
                population[i] = random.sample(range(1, numJobs + 1), numJobs)
            stagnant = 0

        new_population = []
        elite = sorted(population, key=lambda ind: problem.calculateCost(ind, numJobs, dataJobs, dataSetup))[:5]
        new_population.extend(elite)

        for _ in range(pop_size - len(elite)):
            parent1 = random.choice(population)
            parent2 = random.choice(population)
            child = algoritmo_genetico.order_crossover(parent1, parent2)

            adaptive_mutation_rate = mutation_rate * (1 + (0.5 - random.random()))
            if random.random() < adaptive_mutation_rate:
                algoritmo_genetico.mutate_swap(child)

            # Aplica busca tabu apenas nos melhores filhos
            child_cost = problem.calculateCost(child, numJobs, dataJobs, dataSetup)
            if child_cost < (sum(fitness) / len(fitness)):
                child, _ = busca_tabu.busca_tabu(child, numJobs, dataJobs, dataSetup)

            new_population.append(child)

        population = new_population

    gap = problem.gap(best_cost, bestValue)
    return best_ind, best_cost, gap

# Executa o AG com Busca Tabu + Mut. Adaptativa + Diversidade
melhor_solucao_advanced, melhor_custo_advanced, gap_advanced = genetic_algorithm_advanced(numJobs, dataJobs, dataSetup, bestValue)
print("\nAG Avançado (Tabu + Diversidade + Mut. Adaptativa):")
print("Melhor Solução:", melhor_solucao_advanced)
print("Custo...:", melhor_custo_advanced)
print("GAP......: %.2f%%" % gap_advanced)