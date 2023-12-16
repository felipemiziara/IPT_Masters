def clibingPyramid(n, brokenRocks):

    tabulation = [[0 for _ in range(n)] for _ in range(n)]
    """ 
        Setar a base da piramide com todas as possibilidades de início:
            1 - Para as pedras que podem iniciar a subida setar 1;
            2 - Deixe o valor 0 para as pedras estragadas.
    """
    for i in range(n):
        if brokenRocks.get(1) != i + 1:
            tabulation[0][i] = 1

    """
        Agora, é subir a pirâmide de acordo com as regras:
            * - Subir na pedra imediatamente a cima;
            * - Subir na pedra a cima e seguinte;
            * - Subir somente em pedras não defeituosas.
        
        O For começa em 1 pois a primeira linha, como a estragégia
        dinâmica foi a tabulation, estamos indo bottom-up, desta 
        forma a inicialização da primeira linha foi necessária.
    """        
    for i in range(1, n):
        """
            n - 1: Aqui para ganhar eficiência, só processamos de fato as pedras
            que fazem parte da pirâmide, porém usamos a estrutura de matriz.
        """
        for j in range(n - i):
            if brokenRocks.get(i+1) != j + 1 :
                tabulation[i][j] = tabulation[i - 1][j] + tabulation[i - 1][j + 1]
    # De acordo com a estratégia bottom-up, a soma de todas as possibilidades fica
    #   no topo da pirâmede, que é a posição P (N-1, 0)
    return tabulation[n-1][0]

if __name__ == "__main__": 
    nivel = 4
    qtdPedras = 2
    pedras = {}
    pedras[2] = 1
    pedras[3] = 2

    print(f"Número de possibilidades diferentes: {clibingPyramid(nivel, pedras)}")

    nivel = 5
    qtdPedras = 3
    pedras = {}
    pedras[3] = 2
    pedras[2] = 3
    pedras[1] = 4

    print(f"Número de possibilidades diferentes: {clibingPyramid(nivel, pedras)}")
