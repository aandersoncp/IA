def movimentacao(matriz_original):
    """ Indica os possíves movimentos da matriz passada """

    """ Verificando a posição do 0, e obtendo o indice na matriz """
    movimentos = []
    matriz_atual = eval(matriz_original)
    i, j = 0, 0
    while 0 not in matriz_atual[i]: i += 1
    j = matriz_atual[i].index(0)
    
    """" Analisando a posição do 0, e realizando movimentos válidos """
    """" movendo o 0 para baixo """
    if i<2:
        matriz_atual[i][j], matriz_atual[i+1][j] = matriz_atual[i+1][j], matriz_atual[i][j] 
        movimentos.append(str(matriz_atual))
        matriz_atual[i][j], matriz_atual[i+1][j] = matriz_atual[i+1][j], matriz_atual[i][j] 
    """" movendo o 0 para cima """
    if i>0:
        matriz_atual[i][j], matriz_atual[i-1][j] = matriz_atual[i-1][j], matriz_atual[i][j]  
        movimentos.append(str(matriz_atual)) 
        matriz_atual[i][j], matriz_atual[i-1][j] = matriz_atual[i-1][j], matriz_atual[i][j]
    """" movendo o 0 para a direita """
    if j<2:
        matriz_atual[i][j], matriz_atual[i][j+1] = matriz_atual[i][j+1], matriz_atual[i][j] 
        movimentos.append(str(matriz_atual))
        matriz_atual[i][j], matriz_atual[i][j+1] = matriz_atual[i][j+1], matriz_atual[i][j]
    """" movendo o 0 para a esquerda """
    if j>0:
        matriz_atual[i][j], matriz_atual[i][j-1] = matriz_atual[i][j-1], matriz_atual[i][j] 
        movimentos.append(str(matriz_atual))
        matriz_atual[i][j], matriz_atual[i][j-1] = matriz_atual[i][j-1], matriz_atual[i][j]

    return movimentos


def bfs(inicial, esperado):
    banco = [[inicial]]
    nos_explorados = []
    c = 0
    while banco:
        c = c + 1
        i = 0
        caminho = banco[i]
        banco = banco[:i] + banco[i+1:]
        no_atual = caminho[-1]
        if no_atual in nos_explorados: 
            continue
        for movimento in movimentacao(no_atual):
            if movimento in nos_explorados:
                continue
            banco.append(caminho + [movimento])
        nos_explorados.append(no_atual)
        #print("-bfs-", caminho)
        if no_atual == esperado: break
    print("Numero de estados:", c)
    return caminho


def h_pecas_fora(matriz):
    """ heurística número de peças fora do lugar """
    m = eval(matriz)
    num_pecas_fora = 0
    comparador = 1
    for i in range(0,3):
        for j in range(0,3):
            if m[i][j] != comparador:
                num_pecas_fora += 1
            comparador += 1
    return num_pecas_fora


def a_estrela(inicial, esperado):
    banco = [[h_pecas_fora(inicial),inicial]]
    nos_explorados = []
    c = 0
    while banco:
        c = c + 1
        i = 0
        for j in range(1,len(banco)):
            if (banco[i][0]) > (banco[j][0]):
               i = j
        caminho = banco[i]
        banco = banco[:i] + banco[i+1:]
        no_atual = caminho[-1]
        if no_atual in nos_explorados: continue
        for movimento in movimentacao(no_atual):
            if movimento in nos_explorados: continue
            novo = [caminho[0] + h_pecas_fora(movimento) + h_pecas_fora(no_atual)] + caminho[1:] + [movimento] 
            banco.append(novo)
        nos_explorados.append(no_atual)
        #print("-a-", caminho)
        if no_atual == esperado: break
    print("Numero de estados:", c)
    return caminho


m_inicial = str([
                [1,2,0],
                [4,6,3],
                [7,5,8]
            ])

m_final = str([
                [1,2,3],
                [4,5,6],
                [7,8,0]
            ])

print("-Resultado Busca em Largura:")
for i in bfs(m_inicial,m_final):
    print(i)

print("-Resultado A*:")
for i in a_estrela(m_inicial,m_final):
    print(i)