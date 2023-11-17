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
        if(tree.esq is not None): 
            imprimeArvore(tree.esq, nivel +1)
        if(tree.dir is not None):
            imprimeArvore(tree.dir, nivel +1)


arvore = [5,3,7,15,1]
tree = None
for i in arvore:
    tree = insere(tree, TreeNode(i))

imprimeArvore(tree)

def retornaNivel(tree, no, nivel=0):
    if (no is None or tree is None):
        return -1
    if(no == tree.data):
        return nivel
    elif no < tree.data:
        return retornaNivel(tree.esq, no, nivel+1)
    elif no > tree.data:
        return retornaNivel(tree.dir, no, nivel+1)

elemento = 6
print("Nível do elemento " + str(elemento) + ":" + str(retornaNivel(tree,  elemento)))