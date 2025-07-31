import problem
import random

#Busca Tabu
    
def gerar_vizinhos(solucao, numJobs):
    """
    Gera vizinhos da solução atual, realizando trocas entre dois trabalhos da solução.
    Retorna uma lista de soluções vizinhas.
    """
    vizinhos = []
    for i in range(numJobs - 1):
        for j in range(i + 1, numJobs):
            # Cria uma nova solução trocando os trabalhos i e j
            nova_solucao = solucao[:]
            nova_solucao[i], nova_solucao[j] = nova_solucao[j], nova_solucao[i]
            vizinhos.append(nova_solucao)
    
    return vizinhos

def busca_tabu(solution_inicial, numJobs, dataJobs, dataSetup, max_iter=100, max_tabu_size=10):
    # Inicializa a solução corrente e a melhor solução encontrada
    melhor_solucao = solution_inicial
    melhor_custo = problem.calculateCost(melhor_solucao, numJobs, dataJobs, dataSetup)
    
    solucao_corrente = melhor_solucao
    custo_corrente = melhor_custo
    
    # Lista tabu (armazena os movimentos recentes)
    lista_tabu = []
    
    # Número de iterações (loops de busca)
    iteracao = 0
    
    while iteracao < max_iter:
        vizinhos = gerar_vizinhos(solucao_corrente, numJobs)
        melhor_vizinho = None
        melhor_custo_vizinho = float('inf')
        
        # Para cada vizinho, calcular o custo
        for vizinho in vizinhos:
            custo_vizinho = problem.calculateCost(vizinho, numJobs, dataJobs, dataSetup)
            
            # Se o vizinho não está na lista tabu ou é uma solução aspirante
            if (vizinho not in lista_tabu or custo_vizinho < custo_corrente):
                # Aceitar o vizinho se ele for melhor ou é uma solução aspirante
                if custo_vizinho < melhor_custo_vizinho:
                    melhor_vizinho = vizinho
                    melhor_custo_vizinho = custo_vizinho
        
        # Se encontrou um vizinho melhor, atualiza a solução corrente
        if melhor_vizinho:
            solucao_corrente = melhor_vizinho
            custo_corrente = melhor_custo_vizinho
            
            # Se a nova solução é a melhor encontrada até agora, atualiza a melhor solução
            if custo_corrente < melhor_custo:
                melhor_solucao = solucao_corrente
                melhor_custo = custo_corrente
        
        # Atualiza a lista tabu
        lista_tabu.append(solucao_corrente)
        
        # Se a lista tabu atingir o tamanho máximo, remove a solução mais antiga
        if len(lista_tabu) > max_tabu_size:
            lista_tabu.pop(0)
        
        iteracao += 1
    
    return melhor_solucao, melhor_custo
