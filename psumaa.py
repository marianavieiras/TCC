'''

PSUMAA - Problema de sequenciamento de uma máquina com multa por antecipação e atraso.

'''
import sys
import problem

def main():
    print("="*80)
    print("PEP300 - Metaheuristics Techniques for Combinatorial Optimization")
    print("PSUMAA")
    print("-"*80)

    sourceFile = ''
    solutionFile = ''

    try:
        sourceFile = sys.argv[1]
        if len(sys.argv) > 2:
            solutionFile = sys.argv[2]
    except:
        print("Usage: psumaa.py <dataFile> <solutionFile>")
        sys.exit(2)

    numJobs, dataJobs, dataSetup, bestValue = problem.readFiles(sourceFile, solutionFile)

    print("BKS.......: ", bestValue)
    print("-"*80)

    # Call your method here!    

if __name__ == "__main__":
    main()