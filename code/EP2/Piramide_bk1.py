def calculaPiramide(n, nivel, pos, mt):
    # Se a posição ultrapassa o máximo de pedras por nível
    # Ou encontrei uma pedra estragada
    print(f"Trabalhando nivel: {nivel} na posicao: {pos}")
    if (pos > n-1-nivel or pos < 0 or mt[nivel][pos] == -1):
        print(f"-----------PEDRA ou inexistente")
        return 0
    # Se eu cheguei no ultimo block
    elif (nivel == n-1):
        print(f"+++++++++++Chegei no topo")
        return 1
    # Se estou tentando acessar um nível inexistente
    elif ( nivel >= n):
        print(f"-----------Nível inexistente")
        return 0
    else:
        print(f"~~~~~~~~~~~Loop")
        for i in range(0, n-nivel-1):
            mt[nivel][i] = calculaPiramide(n, nivel+1, i,mt) + calculaPiramide(n, nivel+1, i-1,mt)
    return 0

if __name__ == "__main__": 
    nivel = 4
    qtdPedras = 2
    pedras = [[2,1],[3,2]]
    """

    nivel = 5
    qtdPedras = 3
    pedras = [[3,2],[2,3],[1,4]]
    """

    memoizationTable = [[0 for _ in range(nivel)] for _ in range(nivel)]
    for p in pedras:
       memoizationTable[p[0]-1][p[1]-1] = -1

    linhas = nivel
    colunas = nivel
    i = 0
    j = 0
    while i < linhas:
        j = 0
        while j < colunas:
            if(memoizationTable[i][j] != -1):
                memoizationTable[i][j] = 1
            j+=1
        i+=1
        colunas -= 1

    calculaPiramide(nivel, 0, 0, memoizationTable )
    print(f"Número de possibilidades diferentes: {max(memoizationTable[0])}")
    print(memoizationTable)