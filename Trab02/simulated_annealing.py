import random
from tabuleiro import Tabuleiro
from math import *

class SimulatedAnnealing:
    
    def __init__(self, tabuleiro):
        self.tabuleiro = tabuleiro
        self.temperatura = 2000
        self.variacao = 0.99 #Taxa de diminuição da temperatura


    def run(self):
        tabuleiro = self.tabuleiro #Copia o tabuleiro
        tabuleiro_atual = self.tabuleiro.rainhas[:]  #Copia a lista de rainhas
        achou_solucao = False

        if Tabuleiro.calculaConflitos(tabuleiro_atual) == 0: #Testa pra saber se o tabuleiro já é uma solução
            print("Solução:")
            print(Tabuleiro.show(tabuleiro_atual))
            achou_solucao = True
            return
        
        for k in range(0, 1000000000): 
            
            #Realiza a pertubação em uma iteração
            tabuleiro.permutacao(tabuleiro.rainhas) #Vai para a próxima posição vizinha aleatória

            proximo_tabuleiro = tabuleiro.rainhas[:] #guarda as novas posições das rainhas
            delta = Tabuleiro.calculaConflitos(proximo_tabuleiro) - Tabuleiro.calculaConflitos(tabuleiro_atual)
            prob = 0
            if(delta > 0):
                prob = exp((-delta) / (self.temperatura)) #Cálculo da probabilidade

            #Teste de aceitação de uma nova solução
            # Tomada de decisao com base na movimentação(se é boa) e na probabilidade
            if delta < 0 or random.uniform(0, 1) < prob:
                tabuleiro_atual = proximo_tabuleiro[:]
                
            #Testa se não existem conflitos entre as rainhas, solução encontrada! 
            if Tabuleiro.calculaConflitos(tabuleiro_atual) == 0: 
                #print Solução
                print("Solução:")
                print(Tabuleiro.show(tabuleiro_atual))
                achou_solucao = True
                break

            #Redução geometrica da Temperatura
            self.temperatura *= self.variacao

        #caso ao final de todo o Loop principal se encerre sem solução
        if achou_solucao == False:
            print("Não foi possivel encontrar solução.")