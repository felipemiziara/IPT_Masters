class TreeNode:
    def __init__(self, data):
        self.data = data
        self.esq = None
        self.dir = None
        self.alt = 0

#    def __init__(self, data, esq, dir):
#        self.data = data
#        self.esq = esq
#        self.dir = dir
    def __repr__(self):
        return self.data
    def __str__(self):
        return str(self.data)

def altura(node):
    if node is not None:
        return node.alt
    else:
        return 0
    
def insere(tree, elemento):
    if(tree is None):
        tree = elemento
        return tree
    else:
        if (elemento.data < tree.data):
            tree.esq = insere(tree.esq, elemento)
            if (altura(tree.esq) - altura(tree.dir)) == 2:
                if(elemento.data < tree.esq.data):
                    print("rotacao direita")
                    tree = rotacaoDireita(tree)
                else:
                    print("rotacao esquerda direita")
                    tree = rotacaoEsqDireita(tree)
        else:
            tree.dir = insere(tree.dir,elemento)
            if (altura(tree.esq) - altura(tree.dir))==-2:
                if(elemento.data > tree.dir.data):
                    print("rotacao esquerda")
                    tree = rotacaoEsquerda(tree)
                else:
                    print("rotacao direita esquerda")
                    tree = rotacaoDirEsquerda(tree)
        tree.alt = max(altura(tree.esq), altura(tree.dir))+1
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
        if(tree.esq is not None): 
            imprimeArvore(tree.esq, nivel +1)
        if(tree.dir is not None):
            imprimeArvore(tree.dir, nivel +1)

def rotacaoDireita(node):
    aux = node.esq
    node.esq = aux.dir
    aux.dir = node
    node.alt = max(altura(node.esq), altura(node.dir))+1
    aux.alt = max(altura(aux.esq), node.alt) + 1
    return aux

def rotacaoEsquerda(node):
    aux = node.dir
    node.dir = aux.esq
    aux.esq = node
    node.alt = max (altura(node.esq), altura(node.dir))+1
    aux.alt = max (node.alt, altura(aux.dir)) + 1
    return aux

def rotacaoDirEsquerda(node):
    aux = node.dir
    aux.dir = rotacaoDireita(aux)
    return rotacaoEsquerda(node)

def rotacaoEsqDireita(node):
    aux = node.esq
    aux.esq = rotacaoEsquerda(aux)
    return rotacaoDireita(node)

def ordernaAVL(vector):
    avl = None
    for i in vector:
        avl = insere(avl, TreeNode(i))
    return avl
    #inOrdem (avl)
    
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

arvore = [30,10,9,12]

tree = ordernaAVL(arvore)

imprimeArvore(tree)