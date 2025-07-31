import problem
import avaliador
import random

sourceFile = './instances/dados/INST0801.dat'
solutionFile = './instances/saida/inst0801.sol'

numJobs, dataJobs, dataSetup, bestValue = problem.readFiles(sourceFile, solutionFile)

print("Jobs......:", numJobs)

# ------------------- Solução Aleatória -------------------
sol_aleatoria, custo_aleatorio = avaliador.avaliar_aleatoria(numJobs, dataJobs, dataSetup)
print("\nSolução Aleatória:", sol_aleatoria)
print("Custo Inicial...:", custo_aleatorio)

# ------------------- Heurística Construtiva -------------------
sol_heuristica, custo_heuristica, gap_heuristica = avaliador.executar_heuristica(numJobs, dataJobs, dataSetup, bestValue)
print("\nHeurística Construtiva:", sol_heuristica)
print("Custo (Heurística)...:", custo_heuristica)
print("GAP (Heurística)....: %.2f%%" % gap_heuristica)

# ------------------- Busca Local -------------------
random.shuffle(sol_aleatoria)
sol_local, custo_local, gap_local = avaliador.executar_busca_local(sol_aleatoria, numJobs, dataJobs, dataSetup, bestValue)
print("\nBusca Local:", sol_local)
print("Custo (Busca Local)...:", custo_local)
print("GAP (Busca Local)....: %.2f%%" % gap_local)

# ------------------- Busca Tabu -------------------
random.shuffle(sol_aleatoria)
sol_tabu, custo_tabu, gap_tabu = avaliador.executar_tabu(sol_aleatoria, numJobs, dataJobs, dataSetup, bestValue)
print("\nBusca Tabu:", sol_tabu)
print("Custo (Busca Tabu)...:", custo_tabu)
print("GAP (Busca Tabu)....: %.2f%%" % gap_tabu)

# ------------------- Algoritmo Genético -------------------
sol_ag, custo_ag, gap_ag = avaliador.executar_ag(numJobs, dataJobs, dataSetup, bestValue)
print("\nAlgoritmo Genético:", sol_ag)
print("Custo (AG)...:", custo_ag)
print("GAP (AG)....: %.2f%%" % gap_ag)

# # ------------------- Algoritmo Genético Avançado -------------------
# sol_ag_adv, custo_ag_adv, gap_ag_adv = avaliador.executar_ag_avancado(numJobs, dataJobs, dataSetup, bestValue)
# print("\nAG Avançado (Tabu + Diversidade + Mut. Adaptativa):")
# print("Solução:", sol_ag_adv)
# print("Custo...:", custo_ag_adv)
# print("GAP......: %.2f%%" % gap_ag_adv)