class Node:
    def __init__(self, data, prox=None):
        self.data = data
        self.prox = prox

    def __repr__(self):
        return "[" + str(self.data) + "]"
    def __str__(self):
        return "[" + str(self.data) + "]"
    
class LinkedList:
    def __init__(self, cabeca=None):
        self.head = cabeca
        self.tail = None
        self.size = 0


    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node))
            node = node.prox
        nodes.append("None")
        return " -> ".join(nodes)
    
    def addPilha(self, no):
        no.prox = self.head
        self.head = no
        self.size +=1
        if(self.tail is None):
            self.tail = self.head

    def addFila(self, no):
        if(no):
            ele = self.head
            if(ele is None):
                self.head = no 
            #else:
                #while (ele.prox):
                    #ele = ele.prox
                #ele.prox = no
            if (self.tail is not None):
                self.tail.prox = no
            self.tail = no
            self.size +=1
    
    def imprimirNumero(self):
        pilha = LinkedList()
        ele = self.head
        while ele:
            pilha.addPilha(Node(ele.data))
            ele = ele.prox
        print(pilha)


    def imprimir(self):
        print(self)
