def contarDegraus(qtdDegraus, memoizationTable):

    if (qtdDegraus <= 1):
        return 1
 
    if(memoizationTable[qtdDegraus] != -1):
        return memoizationTable[qtdDegraus]
 
    s = contarDegraus(qtdDegraus - 1, memoizationTable) + contarDegraus(qtdDegraus - 2, memoizationTable)
    memoizationTable[qtdDegraus] = s
    return memoizationTable[qtdDegraus]


def calculaPiramide(n, nivel, pos, pedras, mt):
    # Se a posição ultrapassa o máximo de pedras por nível
    # Ou encontrei uma pedra estragada
    print(f">>>>>> nivel: {nivel}; pos: {pos} ")
    if (pedras.get(nivel+1) == pos+1):
        print(f">>>>>>>>>>>>>>> Pedra quebrada ou inexistente ")
        mt[nivel][pos] = 0        
    elif pos > n-1-nivel:
        print(f"========= inexistente")
        return 0       
    elif (nivel == n-1):
        print(f"Cheguei aqui")
        if(mt[nivel][pos] == -1):
            mt[nivel][pos] = 1
        else:
            mt[nivel][pos] += 1
    # Se estou tentando acessar um nível inexistente
    elif ( nivel >= n):
        mt[nivel][pos] = 0
    else:
        print(f"---------- loop")
        for i in range(0, n-nivel-1):
            p1, p2, j = 0,0,nivel+1
            while j < n and mt[j][i] != -1:
                j+=1

            proxNivel = j

            p1 = calculaPiramide(n, proxNivel, i, pedras, mt)
            p2 = calculaPiramide(n, proxNivel, i+1, pedras, mt)
            mt[nivel][i] = p1+p2

    return mt[nivel][pos] 

def calculaPiramide2(n, nivel, pos, pedras, mt):
    # Se a posição ultrapassa o máximo de pedras por nível
    # Ou encontrei uma pedra estragada
    print(f">>>>>> nivel: {nivel}; pos: {pos} ")
    if (pedras.get(nivel+1) == pos+1):
        print(f">>>>>>>>>>>>>>> Pedra quebrada ou inexistente ")
        mt[nivel][pos] = 0        
    elif pos > n-1-nivel:
        print(f"========= inexistente")
        mt[nivel][pos] = -1       
    elif (nivel == n-1):
        print(f"Cheguei aqui")
        if(mt[nivel][pos] == -1):
            mt[nivel][pos] = 1
        else:
            mt[nivel][pos] += 1
    # Se estou tentando acessar um nível inexistente
    elif ( nivel >= n):
        mt[nivel][pos] = 0
    else:
        print(f"---------- loop")
        for i in range(0, n-nivel-1):
            proxNivel = nivel +1
            p1, p2 = 0,0
            if ( mt[nivel][i] == -1):
                p1 = calculaPiramide(n, proxNivel, i, pedras, mt)
                p2 = calculaPiramide(n, proxNivel, i+1, pedras, mt)
                mt[nivel][i] = p1+p2
            else:
                mt[nivel][i] = 1


    return mt[nivel][pos] 

if __name__ == "__main__": 
    nivel = 4
    qtdPedras = 2
    pedras = {}
    pedras[2] = 1
    pedras[3] = 2
    memoizationTable = [[-1 for _ in range(nivel)] for _ in range(nivel)]

    print(f"Número de possibilidades diferentes: {calculaPiramide(nivel,0, 0, pedras, memoizationTable)}")
    print(memoizationTable)
"""
    nivel = 5
    qtdPedras = 3
    pedras = {}
    pedras[3] = 2
    pedras[2] = 3
    pedras[1] = 4
    memoizationTable = [[-1 for _ in range(nivel)] for _ in range(nivel)]
    print(f"Número de possibilidades diferentes: {calculaPiramide(nivel,0, 0, pedras, memoizationTable)}")
    print(memoizationTable)
"""
