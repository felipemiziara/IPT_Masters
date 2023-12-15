def calculaPiramide(n, nivel, pos, pedras, mt):
    # Se a posição ultrapassa o máximo de pedras por nível
    # Ou encontrei uma pedra estragada
    #print(f"Posição: nivel = {nivel}, pos = {pos}")
    if(mt[nivel+1][i] != 0):
                return mt[nivel][i]
    if (pos > n-1-nivel or pedras.get(nivel+1) == pos+1):
        return 0
    # Se eu cheguei no ultimo block
    elif (nivel == n-1):
        return 1
    # Se estou tentando acessar um nível inexistente
    elif ( nivel >= n):
        return 0
    else:
        for i in range(0, n-nivel-1):
      
            mt[nivel] = calculaPiramide(n, nivel+1, i, pedras, mt) + calculaPiramide(n, nivel+1, i+1, pedras,mt)
    return

if __name__ == "__main__": 
    nivel = 4
    qtdPedras = 2
    pedras = {}
    pedras[2] = 1
    pedras[3] = 2
    memoizationTable = [[0 for _ in range(nivel)] for _ in range(nivel)]

    print(f"Número de possibilidades diferentes: {calculaPiramide(nivel,0, 0, pedras, memoizationTable)}")