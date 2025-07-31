import problem
import random
import heuristica_construtiva
import busca_local
import busca_tabu

# ------------------- LEITURA DOS ARQUIVOS -------------------

# Primeira instância (exemplo com 4 jobs)
sourceFile = './instances/instpaper.dat'
solutionFile = ''
numJobs, dataJobs, dataSetup, bestValue = problem.readFiles(sourceFile, solutionFile)

# Criando solução inicial fixa para essa instância
solution = [3, 4, 1, 2]
cost = problem.calculateCost(solution, numJobs, dataJobs, dataSetup)
print("Solução Inicial (Aleatória):", solution)
print("Custo Inicial...: ", cost)

# Segunda instância (exemplo com 8 jobs)
sourceFile = './instances/dados/INST0801.dat'
solutionFile = './instances/saida/inst0801.sol'
numJobs, dataJobs, dataSetup, bestValue = problem.readFiles(sourceFile, solutionFile)

# Gerando uma solução inicial aleatória
solution = list(range(1, numJobs + 1))
random.shuffle(solution)

print("\nSolução Inicial (Aleatória):", solution)
cost = problem.calculateCost(solution, numJobs, dataJobs, dataSetup)
print("Custo Inicial...: ", cost)

gap = problem.gap(cost, bestValue)
print("Best value......: ", bestValue)
print("Solution Cost...: ", cost)
print("GAP.............: ", '%.2f'%gap)

# ------------------- HEURÍSTICA CONSTRUTIVA -------------------

# Exibe a solução inicial antes de aplicar a heurística construtiva
print("\nAntes da Heurística Construtiva:")
print("Solução Inicial:", solution)
print("Custo Inicial...: ", cost)

# Aplicando uma heurística gulosa para gerar uma solução inicial
solucao_heuristica = heuristica_construtiva.greedy_construction(numJobs, dataJobs, dataSetup)
custo_heuristica = problem.calculateCost(solucao_heuristica, numJobs, dataJobs, dataSetup)
gap_heuristica = problem.gap(custo_heuristica, bestValue)

print("\nHeurística Construtiva Parcialmente Gulosa:")
print("Solução Heurística:", solucao_heuristica)
print("Custo (Heurística)...: ", custo_heuristica)
print("GAP (Heurística)....: ", '%.2f' % gap_heuristica)

# ------------------- BUSCA LOCAL -------------------

# Exibe a solução inicial antes de aplicar a busca local
print("\nAntes da Busca Local:")
solution_local = list(range(1, numJobs + 1))
random.shuffle(solution_local)
cost_local = problem.calculateCost(solution_local, numJobs, dataJobs, dataSetup)
print("Solução Inicial:", solution_local)
print("Custo Inicial...: ", cost_local)

# Aplicando busca local
solution_local, cost_local = busca_local.local_search(solution_local, numJobs, dataJobs, dataSetup)
gap_local = problem.gap(cost_local, bestValue)

print("\nBusca Local (Decida) - 2-opt:")
print("Solução Refinada (Local Search):", solution_local)
print("Custo (Busca Local)...: ", cost_local)
print("GAP (Busca Local)....: ", '%.2f' % gap_local)

# ------------------- BUSCA TABU -------------------

# Exibe a solução inicial antes de aplicar a busca tabu
print("\nAntes da Busca Tabu:")
solution_tabu = list(range(1, numJobs + 1))
random.shuffle(solution_tabu)
cost_tabu = problem.calculateCost(solution_tabu, numJobs, dataJobs, dataSetup)
print("Solução Inicial:", solution_tabu)
print("Custo Inicial...: ", cost_tabu)

# Aplicando busca tabu
melhor_solucao, melhor_custo = busca_tabu.busca_tabu(solution_tabu, numJobs, dataJobs, dataSetup)
gap_tabu = problem.gap(melhor_custo, bestValue)
print("\nBusca Tabu:")
print("Solução Refinada (Tabu):", melhor_solucao)
print("Custo (Busca Tabu)...: ", melhor_custo)
print("GAP (Busca Tabu)....: ", '%.2f' % gap_tabu)

# ------------------- HÍBRIDOS -------------------

# 1. Heurística Construtiva + Busca Local
print("\nAntes do Híbrido: Heurística Construtiva + Busca Local")
solucao_hb1 = heuristica_construtiva.greedy_construction(numJobs, dataJobs, dataSetup)
custo_hb1 = problem.calculateCost(solucao_hb1, numJobs, dataJobs, dataSetup)
print("Solução Inicial:", solucao_hb1)
print("Custo Inicial...: ", custo_hb1)

solucao_hb1, custo_hb1 = busca_local.local_search(solucao_hb1, numJobs, dataJobs, dataSetup)
gap_hb1 = problem.gap(custo_hb1, bestValue)
print("\nHíbrido: Heurística Construtiva + Busca Local")
print("Solução Híbrida:", solucao_hb1)
print("Custo (Híbrido 1)...: ", custo_hb1)
print("GAP (Híbrido 1)....: ", '%.2f' % gap_hb1)

# 2. Heurística Construtiva + Busca Tabu
print("\nAntes do Híbrido: Heurística Construtiva + Busca Tabu")
solucao_hb2 = heuristica_construtiva.greedy_construction(numJobs, dataJobs, dataSetup)
custo_hb2 = problem.calculateCost(solucao_hb2, numJobs, dataJobs, dataSetup)
print("Solução Inicial:", solucao_hb2)
print("Custo Inicial...: ", custo_hb2)

solucao_hb2, custo_hb2 = busca_tabu.busca_tabu(solucao_hb2, numJobs, dataJobs, dataSetup)
gap_hb2 = problem.gap(custo_hb2, bestValue)
print("\nHíbrido: Heurística Construtiva + Busca Tabu")
print("Solução Híbrida:", solucao_hb2)
print("Custo (Híbrido 2)...: ", custo_hb2)
print("GAP (Híbrido 2)....: ", '%.2f' % gap_hb2)

# 3. Busca Tabu com Inicialização via Busca Local
print("\nAntes do Híbrido: Busca Tabu com Inicialização via Busca Local")
solucao_hb3 = list(range(1, numJobs + 1))
random.shuffle(solucao_hb3)
custo_hb3 = problem.calculateCost(solucao_hb3, numJobs, dataJobs, dataSetup)
print("Solução Inicial:", solucao_hb3)
print("Custo Inicial...: ", custo_hb3)

solucao_hb3, custo_hb3 = busca_local.local_search(solucao_hb3, numJobs, dataJobs, dataSetup)
solucao_hb3, custo_hb3 = busca_tabu.busca_tabu(solucao_hb3, numJobs, dataJobs, dataSetup)
gap_hb3 = problem.gap(custo_hb3, bestValue)
print("\nHíbrido: Busca Tabu com Inicialização via Busca Local")
print("Solução Híbrida:", solucao_hb3)
print("Custo (Híbrido 3)...: ", custo_hb3)
print("GAP (Híbrido 3)....: ", '%.2f' % gap_hb3)

# Busca Local com Inicialização via Heurística Construtiva
print("\nAntes do Híbrido: Busca Local com Inicialização via Heurística Construtiva")
solucao_hb4 = heuristica_construtiva.greedy_construction(numJobs, dataJobs, dataSetup)
custo_hb4 = problem.calculateCost(solucao_hb4, numJobs, dataJobs, dataSetup)
print("Solução Inicial:", solucao_hb4)
print("Custo Inicial...: ", custo_hb4)

solucao_hb4, custo_hb4 = busca_local.local_search(solucao_hb4, numJobs, dataJobs, dataSetup)
gap_hb4 = problem.gap(custo_hb4, bestValue)
print("\nHíbrido: Busca Local com Inicialização via Heurística Construtiva")
print("Solução Híbrida:", solucao_hb4)
print("Custo (Híbrido 4)...: ", custo_hb4)
print("GAP (Híbrido 4)....: ", '%.2f' % gap_hb4)

# Busca Local + Busca Tabu
print("\nAntes do Híbrido: Busca Local + Busca Tabu")
solucao_hb6 = list(range(1, numJobs + 1))
random.shuffle(solucao_hb6)
custo_hb6 = problem.calculateCost(solucao_hb6, numJobs, dataJobs, dataSetup)
print("Solução Inicial:", solucao_hb6)
print("Custo Inicial...: ", custo_hb6)

# Busca Local
solucao_hb6, custo_hb6 = busca_local.local_search(solucao_hb6, numJobs, dataJobs, dataSetup)
# Busca Tabu
solucao_hb6, custo_hb6 = busca_tabu.busca_tabu(solucao_hb6, numJobs, dataJobs, dataSetup)
gap_hb6 = problem.gap(custo_hb6, bestValue)
print("\nHíbrido: Busca Local + Busca Tabu")
print("Solução Híbrida:", solucao_hb6)
print("Custo (Híbrido 6)...: ", custo_hb6)
print("GAP (Híbrido 6)....: ", '%.2f' % gap_hb6)

# Busca Local + Busca Tabu com Inicialização via Heurística Construtiva
print("\nAntes do Híbrido: Busca Local + Busca Tabu com Inicialização via Heurística Construtiva")
solucao_hb8 = heuristica_construtiva.greedy_construction(numJobs, dataJobs, dataSetup)
custo_hb8 = problem.calculateCost(solucao_hb8, numJobs, dataJobs, dataSetup)
print("Solução Inicial:", solucao_hb8)
print("Custo Inicial...: ", custo_hb8)

# Busca Local
solucao_hb8, custo_hb8 = busca_local.local_search(solucao_hb8, numJobs, dataJobs, dataSetup)
# Busca Tabu
solucao_hb8, custo_hb8 = busca_tabu.busca_tabu(solucao_hb8, numJobs, dataJobs, dataSetup)
gap_hb8 = problem.gap(custo_hb8, bestValue)
print("\nHíbrido: Busca Local + Busca Tabu com Inicialização via Heurística Construtiva")
print("Solução Híbrida:", solucao_hb8)
print("Custo (Híbrido 8)...: ", custo_hb8)
print("GAP (Híbrido 8)....: ", '%.2f' % gap_hb8)
