import numpy as np
import random
import problem

def greedy_construction(numJobs, dataJobs, dataSetup, alpha=0.3):
    """
    Heurística Construtiva Parcialmente Gulosa
    
    Na heurística construtiva, o primeiro elemento é escolhido com um critério guloso, mas com um fator aleatório.
    """
    candidate_list = list(range(1, numJobs + 1))  # Lista com todos os jobs disponíveis
    solution = []  # Solução inicial vazia
    
    while candidate_list:
        costs = []  # Lista para armazenar os custos de cada possível escolha
        
        # Calcula o custo de adicionar cada trabalho candidato à solução
        for job in candidate_list:
            partial_solution = solution + [job]  # Solução parcial ao adicionar esse trabalho
            cost = problem.calculateCost(partial_solution, len(partial_solution), dataJobs, dataSetup)
            costs.append((job, cost))
        
        # Ordena os trabalhos pelo custo (menor custo primeiro)
        costs.sort(key=lambda x: x[1])
        
        # Define o limite de escolha baseado no fator 'alpha'
        max_index = max(1, int(alpha * len(costs)))
        
        # Escolhe aleatoriamente um dos 'melhores' candidatos
        chosen = random.choice(costs[:max_index])[0]
        
        # Adiciona o escolhido à solução e remove da lista de candidatos
        solution.append(chosen)
        candidate_list.remove(chosen)
    
    return solution
