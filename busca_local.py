import numpy as np
import random
import problem

def local_search(solution, numJobs, dataJobs, dataSetup):
    """
    Busca Local (Decida)
    
    Na busca local, os primeiros elementos analisados sempre começam pelos primeiros pares na solução atua
    """
    improved = True  # Indica se houve melhoria
    best_cost = problem.calculateCost(solution, numJobs, dataJobs, dataSetup)  # Custo inicial da solução
    best_solution = solution.copy()  # Copia da melhor solução encontrada
    
    while improved:
        improved = False  # Reinicia o estado de melhoria
        
        # Percorre os trabalhos tentando trocas
        for i in range(numJobs - 1):
            for j in range(i + 1, numJobs):
                # Cria uma nova solução trocando os trabalhos nos índices i e j
                new_solution = best_solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                
                # Calcula o custo da nova solução
                new_cost = problem.calculateCost(new_solution, numJobs, dataJobs, dataSetup)
                
                # Se a nova solução for melhor, atualiza a melhor solução
                if new_cost < best_cost:
                    best_solution = new_solution[:]
                    best_cost = new_cost
                    improved = True  # Indica que houve melhoria
                    break  # Reinicia a busca local
            if improved:
                break
    
    return best_solution, best_cost