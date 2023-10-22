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
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    
#inicia tudo
    
llist = LinkedList()
first_node = Node(17)
llist.head = first_node
second_node = Node(31)
third_node = Node(2)
fourth_node = Node(1)

llist.head.next = second_node
second_node.next=third_node
third_node.next = fourth_node

print(llist)

def minimo(l, m):
    if l == None :
        return m
    else:
        if l.data < m:
            m = l.data
        return minimo(l.next, m)



def inverterLista(l, pivo, esq, dir):

    if l==None or pivo is None or dir is None:
        return l
    else:
        pivo.next = dir.next
        dir.next = esq
        l.head = dir
        return inverterLista(l, pivo, dir, pivo.next)



def inserirKesima(l, esq, pivo, ele, k, count):
    if l is not None:
        if k == count:      #achei a posição correta
            if(k==1):       #se for a primeira posição, troca a cabeça
                l.head = ele
            else:           #se for qualquer outra posição aponta o anterior para ele
                esq.next = ele
            ele.next=pivo   #o novo elemente aponta para o próximo (mesmo que o próximo seja nulo)
        elif count < k and pivo is not None: #
            return inserirKesima(l, pivo, pivo.next, ele, k, count +1)
    return l

#print (str(minimo(llist.head, llist.head.data)))

#print (inverterLista(llist, llist.head, llist.head, llist.head.next))
 
#print (inserirKesima(llist, None, llist.head, Node(56), 6, 1))

def inserirListaOrdenada (first, ele):
    no = first
    prev = None
    if(first is  None):
        first = ele
        ele.next = ele
    else:
        while ele.data < no.data and first != no.next:
            no = no.next
        prev = no.next
        no.next = ele
        ele.next = prev
    return first

lista = LinkedList() 

lista.head = inserirListaOrdenada(None, Node(5))
#inserirListaOrdenada(lista.head, Node(2))

print (lista)