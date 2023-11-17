class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data
    def __str__(self):
        return str(self.data)
    
class LinkedList:
    def __init__(self):
        self.first = None
        self.size = 0

    def __repr__(self):
        node = self.first
        nodes = []
        for i in range(self.size):
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    
llist = LinkedList()
first_node = Node(17)
llist.head = first_node
second_node = Node(31)
third_node = Node(2)
fourth_node = Node(1)

llist.head.next = second_node
second_node.next=third_node
third_node.next = fourth_node

def inserirListaOrdenada (l, ele):
    no = l.first #primeiro elemento da lista
    prev = None
    cont = 1
    if(l.first is  None):
        l.first = ele
        ele.next = ele
        l.size = 1
    else:
        while ele.data > no.data and cont <= l.size+1:
            prev = no
            no = no.next
            cont+=1
        ele.next = no
        print ("Inserindo ele: " + str(ele.data))
        if(prev is not None):
            print ("prev: " + str(prev.data))
        print ("frente: " +str(no.data))
        if(prev is None):
            l.first = ele
        else:
            prev.next = ele
        l.size += 1
        print(l)
    return l


def buscaListaOrdenada(l, ele):
    no = l.first
    cont = 1
    if(l is None or ele is None):
        return None
    else:
        while no.data < ele.data and cont <= l.size:
            no = no.next
            cont += 1
        if (cont <= l.size and ele.data == no.data):
            return no
        else:
            return None

def removeListaOrdenada(l, ele):
    no = l.first.next
    cont = 1
    prev = l.first
    if(l is not None and ele is not None):
        while no.data != ele.data and cont <= l.size:
            print(no.data)
            prev = no
            no = no.next
            cont += 1
        if (cont <= l.size and ele.data == no.data):
            prev.next = no.next
            if (cont == l.size): # se for o primeiro elemento da lista, atualiza o primeiro
                l.first = no.next
            l.size-=1    
    return l


lista = LinkedList() 

inserirListaOrdenada(lista, Node(5))
#print (lista)
inserirListaOrdenada(lista, Node(2))
#print (lista)
inserirListaOrdenada(lista, Node(4))
#print (lista)
inserirListaOrdenada(lista, Node(7))
print (lista)


#n = buscaListaOrdenada(lista, Node(5)) 
#print ("Ultimo no: " + str(n.data))
#print ("Aponta para: " + str(n.next.data))

#print (removeListaOrdenada(lista, Node(1)))


#inserirListaOrdenada(lista.head, Node(2))