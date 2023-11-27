from LinkedList import *
class Graph: 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = []
  
    def addEdge(self, v, listaAdjacentes): 
        self.graph.append(listaAdjacentes) 
  
    def printGraph(self):
        for v in self.graph:
            print(f"{v}:")
            for u in self.graph[v]:
                print(f"  -> {u}")
    
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

def main():
    g = Graph(10) 
    
    graph = {
        1: [2,5,6],
        2: [1,3,7],
        3: [2,4,8],
        4: [3,5,9],
        5: [4,1,10],
        6: [1,8,9],
        7: [2,9,10],
        8: [3,6,10],
        9: [4,6,7],
        10:[5,7,8]
    }

    #Constroi grafo de Pertersen, primeiro pelos nós externos.
    l1 = LinkedList(Node(1))
    l1.addFila(Node(2))
    l1.addFila(Node(5))
    l1.addFila(Node(6))
    g.addEdge(l1)

    l2 = LinkedList(Node(2))
    l2.addFila(Node(1))
    l2.addFila(Node(3))
    l2.addFila(Node(7))
    g.addEdge(l2)

    l3 = LinkedList(Node(3))
    l3.addFila(Node(2))
    l3.addFila(Node(4))
    l3.addFila(Node(8))
    g.addEdge(l3)

    l4 = LinkedList(Node(4))
    l4.addFila(Node(3))
    l4.addFila(Node(5))
    l4.addFila(Node(9))
    g.addEdge(l4)

    l5 = LinkedList(Node(5))
    l5.addFila(Node(4))
    l5.addFila(Node(1))
    l5.addFila(Node(10))
    g.addEdge(l5)

    #Nós internos
    l6 = LinkedList(Node(6))
    l6.addFila(Node(1))
    l6.addFila(Node(8))
    l6.addFila(Node(9))
    g.addEdge(l6)

    l7 = LinkedList(Node(7))
    l7.addFila(Node(2))
    l7.addFila(Node(9))
    l7.addFila(Node(10))
    g.addEdge(l7)

    l8 = LinkedList(Node(8))
    l8.addFila(Node(3))
    l8.addFila(Node(6))
    l8.addFila(Node(10))
    g.addEdge(l8)

    l9 = LinkedList(Node(9))
    l9.addFila(Node(4))
    l9.addFila(Node(6))
    l9.addFila(Node(7))
    g.addEdge(l9)

    l10 = LinkedList(Node(10))
    l10.addFila(Node(5))
    l10.addFila(Node(7))
    l10.addFila(Node(8))
    g.addEdge(l10)

    g.printGraph()

if __name__ == "__main__":
    main()
