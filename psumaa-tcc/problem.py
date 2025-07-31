'''

PSUMAA - Problema de sequenciamento de uma máquina com multa por antecipação e atraso.

'''

import math
import numpy as np
import codecs

def readFiles(dataFile, solutionFile):
    print("Reading files...")
    print("Data......: ", dataFile)
    print("Solution..: ", solutionFile)
    
    data = open(dataFile)
    numJobs = 0

    for i, line in enumerate(data):
        ln = line.split()

        # Number of Jobs:
        if i == 0:
            numJobs = int(ln[ len(ln) - 1 ])
            # id, Pi Ei Ti Alphai Betai
            dataJobs = np.zeros(shape=(numJobs, 6))
            dataSetup = np.zeros(shape=(numJobs, numJobs))

            print("Jobs......: ", numJobs)
        # Data jobs    
        elif i > 0 and i <= numJobs:
            for j in range(0, 6):
                dataJobs[i - 1][j] = int(ln[j])
        # Setup times job x job
        elif i > numJobs:
            # print(ln) 
            if len(line) > 0:
                # Line of job / setup
                k = i - numJobs - 1
                # print(k)
                for j in range(0, numJobs):
                    dataSetup[k][j] = int(ln[j])

    data.close()

    # Solution:
    # BKS
    bestValue = np.inf

    # If there is a solution file:
    if len(solutionFile) > 0:
        with codecs.open(solutionFile, 'r', encoding='utf-8', errors='ignore') as solution:
            for i, line in enumerate(solution):
                ln = line.split()

                # print(ln)

                # Value:
                if i == 2:
                    bestValue = float(ln[2])
                    break
        solution.close()

    # print(numJobs, dataJobs, dataSetup, bestValue)
    return numJobs, dataJobs, dataSetup, bestValue

# Solution -> array[1:numJobs]
def calculateCost(solution, numJobs, dataJobs, dataSetup):

    time = 0
    alphaCost = 0.0
    betaCost = 0.0
    solutionCost = 0.0

    for i in range(0, numJobs):

        job = solution[i] - 1

        time = time + dataJobs[job][1] # Pi

        # Earliness and tardiness
        # Checking earliness
        if time < dataJobs[job][2]: # Ei
            alphaCost = alphaCost + ( dataJobs[job][2] - time ) * dataJobs[job][4] # Alpha_i
        # Checking tardiness
        elif time > dataJobs[job][3]: # Ti
            betaCost = betaCost + ( time - dataJobs[job][3] ) * dataJobs[job][5] # Beta_i

        # Setup time:
        # If it is not in the last job:
        if i + 1 < numJobs:
            # Next job
            jobj = solution[i + 1] - 1
            time = time + dataSetup[job][jobj]

    # print("Alpha.....: ", alphaCost)
    # print("Beta......: ", betaCost)
    # print("Time......: ", time)

    solutionCost = alphaCost + betaCost

    return solutionCost

def gap(cost, bestValue):

    return (( cost - bestValue ) / bestValue) * 100.0
