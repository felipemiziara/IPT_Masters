from LinkedList import *
class Graph: 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph =[]
        self.visita = []
        self.cores = []
  
    def addEdge(self,listaAdjacentes):
        self.graph.append(listaAdjacentes) 
  
    def printGraph(self):
        for v in range(self.V):
            print(f"{self.graph[v][0]}:")
            for u in range(1,len(self.graph[v])):
                print(f"  -> {self.graph[v][u]}")
    
    def find(self, parent, i): 
        if parent[i] != i:  
            parent[i] = self.find(parent, parent[i]) 
        return parent[i] 
  
    def union(self, parent, rank, x, y): 
        if rank[x] < rank[y]: 
            parent[x] = y 
        elif rank[x] > rank[y]: 
            parent[y] = x 
  
        else: 
            parent[y] = x 
            rank[x] += 1
    
    def greedyColoring(self):
        graph = self.graph
        cores = [-1] * (self.V+1)

        #colore o primeiro vertice
        cores[graph[0][0]] = 0

        #inicia com todas as cores disponíveis
        coresDisponiveis = [True] * (self.V+1)

        nl = '\n'

        for u in range(1 ,self.V):

            for adj in range(1, len(graph[u])):
                #Se algum vértice adjacente já foi colorido (!= -1) marca aquela cor como indisponível
                if (cores[graph[u][adj]] != -1):
                    print(f"{nl}========> Setando indisponibilidade: ")
                    print(f"=============> It: {u}, It adj: {adj}, Vertice: {graph[u][0]}, Adj: {graph[u][adj]}")
                    coresDisponiveis[cores[graph[u][adj]]] = False

            cor = 0

            #Aqui é o passo Guloso, procura a primeira Cor disponível
            while cor <= self.V: 
                if coresDisponiveis[cor] == True:
                    break
                cor +=1

            #Colore o vértice com a cor escolhida.
            cores[graph[u][0]] = cor
            print(" ")
            print(f"******* It:{u} ---> Atualizando cores= {cores}")
            print(f"******* It:{u} ---> Atualizando cores= {coresDisponiveis}")
            print(" ")
            #Reseta as cores disponíveis para dar a opção de ter uma escolha gulosa.
            for adj in range(1, len(graph[u])):
                if (cores[graph[u][adj]] != -1):
                    coresDisponiveis[cores[graph[u][adj]]] = True

        for u in range(self.V):
            print (f"id: {u} -> Vertice {graph[u][0]} ----> Cor: {cores[graph[u][0]]}")
        return max(cores)+1

def main():
    g1 = Graph(10) 
    #Definindo uma matrix onde a coluna 0 são os vértices e as demais a lista de adjacentes
    graph1 = [
        [1,2,5,6],
        [2,1,3,7],
        [3,2,4,8],
        [4,3,5,9],
        [5,4,1,10],
        [6,1,8,9],
        [7,2,9,10],
        [8,3,6,10],
        [9,4,6,7],
        [10,5,7,8]
    ]

    g1.graph = graph1
    g1.printGraph()

    print(f"Quantidade de cores no grafo = {g1.greedyColoring()}")
    
    g2 = Graph(5) 
    graph2 = [
        [0,1,2],
        [1,0,2,4],
        [2,0,1,4],
        [3,4],
        [4,1,2,3]
    ]
    g2.graph = graph2
    g2.printGraph()

    print(f"Quantidade de cores no grafo = {g2.greedyColoring()}")


    g3 = Graph(8) 
    graph3 = [
        [1,6,7,8],
        [2,5,7,8],
        [3,5,6,8],
        [4,5,6,7],
        [5,2,3,4],
        [6,1,3,4],
        [7,1,2,4],
        [8,1,2,3]
    ]
    g3.graph = graph3
    #g3.printGraph()

    #print(f"Quantidade de cores no grafo = {g3.greedyColoring()}")


    g4 = Graph(8) 
    graph4 = [
        [1,6,7,8],
        [5,2,3,4],
        [2,5,7,8],
        [6,1,3,4],
        [3,5,6,8],
        [7,1,2,4],
        [4,5,6,7],
        [8,1,2,3]
    ]
    g4.graph = graph4
    g4.printGraph()

    print(f"Quantidade de cores no grafo = {g4.greedyColoring()}")

if __name__ == "__main__":
    main()
