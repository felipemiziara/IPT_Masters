import math


class Node:
    def __init__(self, prod, pow):
        self.prod = prod
        self.pow = pow
        self.next = None

    def __repr__(self):
        return "[" + str(self.prod) + "," + str(self.pow) + "]"
    def __str__(self):
        return "[" + str(self.prod) + "," + str(self.pow) + "]"
    
class LinkedList:
    def __init__(self):
        self.head = Node(-1, None)

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    
llpoli = LinkedList()

node1 = Node(5, 10)
node2 = Node(-3,5)
node3 = Node (4, 1)

node1.next = node2
node2.next = node3

llpoli.head.next = node1

print (llpoli)

def calculaPoli(ele, x):
    if ele is None:
        return 0
    else:
        calc = 0
        if ele.prod != -1:
            calc = math.pow(x, ele.pow)*ele.prod
        return calc + calculaPoli(ele.next, x)
        
print(str(calculaPoli(llpoli.head, 2)))

llpoli2 = LinkedList()
print(str(calculaPoli(llpoli2.head, 2)))

poli1 = LinkedList()
poli2 = LinkedList()


n1 = Node(5, 10)
n2 = Node(-3,5)
n3 = Node (4, 1)

n1.next = n2
n2.next = n3

poli1.head.next=n1

m1 = Node(2, 4)
m2 = Node(-2,3)
m3 = Node (1, 2)
m4 = Node (26, 1)

m1.next = m2
m2.next = m3
m3.next = m4

poli2.head.next = m1

def somaPoli(poli1, poli2, x1):
    no = poli1.head
    while no.next is not None:
        no = no.next
    no.next = poli2.head.next
    return calculaPoli(poli1.head, x1)

print(poli1)
print(poli2)

print(calculaPoli(poli1.head, 4))
print(calculaPoli(poli2.head, 4))

print(somaPoli(poli1, poli2, 4))