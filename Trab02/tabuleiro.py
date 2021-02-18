import random

class Tabuleiro:
    def __init__(self, cardinalidade = 40):
        self.cardinalidade = cardinalidade
        self.gerar_tabuleiro()
        
    #gera novo estado do tabuleiro
    def gerar_tabuleiro(self):
        self.rainhas = [0 for i in range(0, self.cardinalidade)] #Coloca 0 em todas as posições
        for i in range(0, self.cardinalidade):
            self.rainhas[i] = random.randint(0, self.cardinalidade - 1) #Coloca cada rainha em uma posição aleatória
    #escolhe aleatoriamente o próximo movimento
    def permutacao(self, rainhas):
        i = random.randint(0, self.cardinalidade - 1) #Escolhe aleatoriamente uma rainha
        j = random.randint(0, self.cardinalidade - 1) #Escolhe a linha que a rainha escolhida vai ocupar, ou seja, o próximo movimento
        while((j == rainhas[i] and self.cardinalidade != 1)): #quantidade diferente de 1
            j = random.randint(0, self.cardinalidade - 1)
        rainhas[i] = j
        return rainhas    

    #calcula a quantidade das ameaças
    def calculaConflitos(rainhas):
        conflitos = 0
        quantidade = len(rainhas)

        for rainha in range(0, quantidade):
            for prox_rainha in range(rainha + 1, quantidade):
                #Verifica se existe ataque entre as rainhas nivel de coluna ou diagonal
                if rainhas[rainha] == rainhas[prox_rainha] or abs(rainha - prox_rainha) == abs(rainhas[rainha] - rainhas[prox_rainha]): #Se rainha e prx_rainha estão na msm linha ou se estão na mesma diagonal
                    conflitos += 1
        return conflitos

    def show(rainhas): #Mostra o resultado do tabuleiro
        board_string = ""
        for row, col in enumerate(rainhas):
            board_string += "(%s, %s)\n" % (row, col)
        return board_string

    def __str__(self): #Função padrão pra mostrar
        board_string = ""
        for row, col in enumerate(self.rainhas):
            board_string += "(%s, %s)\n" % (row, col)
        return board_string
    