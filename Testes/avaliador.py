import problem
import heuristica_construtiva
import busca_local
import busca_tabu
import algoritmo_genetico
import random
import numpy as np


def avaliar_aleatoria(numJobs, dataJobs, dataSetup):
    solucao = random.sample(range(1, numJobs + 1), numJobs)
    custo = problem.calculateCost(solucao, numJobs, dataJobs, dataSetup)
    return solucao, custo


def executar_heuristica(numJobs, dataJobs, dataSetup, bestValue):
    solucao = heuristica_construtiva.greedy_construction(numJobs, dataJobs, dataSetup)
    custo = problem.calculateCost(solucao, numJobs, dataJobs, dataSetup)
    gap = problem.gap(custo, bestValue)
    return solucao, custo, gap


def executar_busca_local(solucao_inicial, numJobs, dataJobs, dataSetup, bestValue):
    solucao, custo = busca_local.local_search(solucao_inicial, numJobs, dataJobs, dataSetup)
    gap = problem.gap(custo, bestValue)
    return solucao, custo, gap


def executar_tabu(solucao_inicial, numJobs, dataJobs, dataSetup, bestValue):
    solucao, custo = busca_tabu.busca_tabu(solucao_inicial, numJobs, dataJobs, dataSetup)
    gap = problem.gap(custo, bestValue)
    return solucao, custo, gap


def executar_ag(numJobs, dataJobs, dataSetup, bestValue):
    solucao, custo, gap = algoritmo_genetico.genetic_algorithm(
        numJobs, dataJobs, dataSetup, bestValue,
        pop_size=100, generations=300, mutation_rate=0.15
    )
    return solucao, custo, gap


def executar_ag_avancado(numJobs, dataJobs, dataSetup, bestValue):
    from teste_of import genetic_algorithm_advanced
    solucao, custo, gap = genetic_algorithm_advanced(numJobs, dataJobs, dataSetup, bestValue)
    return solucao, custo, gap
