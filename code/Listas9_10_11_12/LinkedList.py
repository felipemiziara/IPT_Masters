class Node:
    def __init__(self, data, prox=None, w=1):
        self.data = data
        self.w = w
        self.prox = prox

    def __repr__(self):
        return "[" + str(self.data) + "]"
    def __str__(self):
        return "[" + str(self.data) + "]"
    
class LinkedList:
    def __init__(self, cabeca=None):
        self.head = cabeca
        self.tail = cabeca
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
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.prox
        nodes.reverse()
        return "".join(nodes)

    def imprimir(self):
        print(self)
