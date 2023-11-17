class TreeNode:
    def __init__(self, data):
        self.data = data
        self.esq = None
        self.dir = None

#    def __init__(self, data, esq, dir):
#        self.data = data
#        self.esq = esq
#        self.dir = dir
    def __repr__(self):
        return self.data
    def __str__(self):
        return str(self.data)

def insere(tree, elemento):
    if(tree is None):
        tree = elemento
    else:
        if (elemento.data <= tree.data):
            tree.esq = insere(tree.esq, elemento)
        else:
            tree.dir = insere(tree.dir,elemento)
    return tree

def imprimeArvore(tree, nivel=0):
    if tree is not None :
        head = "└──"
        espacoPai = "    "
        espacoFilho = " " 
        for _ in range(nivel):
            espacoPai += " "
            espacoFilho += " "
        print(espacoPai + espacoFilho + head+ "(" + str (tree.data) + str(")"))
        if(tree.dir is not None):
            imprimeArvore(tree.dir, nivel +1)
        if(tree.esq is not None): 
            imprimeArvore(tree.esq, nivel +1)



arvore = [40, 10, 90, 20, 110, 60, 30, 70, 120,80, 50, 100]
tree = None
for i in arvore:
    tree = insere(tree, TreeNode(i))

imprimeArvore(tree)

def inOrdem(tree):
    pilha = []
    no = tree
    #Lado esquerdo primeiro 
    pilha.append(no)
    while len(pilha):
        if (no.esq is not None):
            pilha.append(no.esq)
        no = pilha.pop()
        print(str(no.data), end= "," )
        if(no.dir is not None):
            pilha.append(no.dir)

def inOrdemCp(tree):
    pilha = []
    node = tree
    while node or pilha:
        if node:
            pilha.append(node)
            node = node.esq
        else:
            node = pilha.pop()
            print(str(node.data), end= "," )
            node = node.dir

inOrdemCp(tree)