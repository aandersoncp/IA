from tabuleiro import Tabuleiro
from simulated_annealing import SimulatedAnnealing


if __name__ == '__main__':
    
    tabuleiro = Tabuleiro()
    print("Rainhas:")
    print(tabuleiro)
    SimulatedAnnealing(tabuleiro).run() 