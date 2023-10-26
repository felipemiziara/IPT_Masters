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

#tree = insere(None, TreeNode(5))
#insere(tree, TreeNode(3))
#insere(tree, TreeNode(7))
#insere(tree, TreeNode(14))
#insere(tree, TreeNode(1))

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

def removeArvore(tree, no, pai=None):
    if (no is None or tree is None):
        return tree
    if(no == tree.data):
        # Situração 1: não tem filhos
        if(tree.esq is None and tree.dir is None):
            if(pai.esq.data == tree.data):
                pai.esq = None
            else:
                pai.dir = None
        else:
            #Situação 2: So tem 1 filho
            if tree.esq is None:
                pai.dir = tree.dir
            elif tree.dir is None:
                pai.esq = tree.esq
            else:
                #Situação 3: Tem 2 filhos vou para a direita
                aux = tree
                auxDir = tree.dir
                while (auxDir.esq is not None):
                    aux = auxDir
                    auxDir=auxDir.esq
                tree.data = auxDir.data
                if(aux.data == tree.data):
                    aux.dir=auxDir.dir
                else:
                    aux.esq = auxDir.dir
    else:
        if(no < tree.data):
            removeArvore(tree.esq, no, tree)
        else:
            removeArvore(tree.dir, no, tree)        




elemento = 20
print("Nível do elemento " + str(elemento) + ":" + str(retornaNivel(tree,  elemento)))

print("---------Removendo 100 ----------")
removeArvore(tree, 100)
imprimeArvore(tree)
print("---------Removendo 20 ----------")
removeArvore(tree, 20)
imprimeArvore(tree)
print("---------Removendo 90 ----------")
removeArvore(tree, 90)
imprimeArvore(tree)


#Exercício 3
def verifyStructure(tree1, tree2):
    if(tree1 is None and tree2 is None):
        return True
    elif(tree1 is not None and tree2 is not None):
        return verifyStructure(tree1.esq, tree2.esq) and verifyStructure(tree1.dir, tree2.dir)
    else:
        return False
        

arvore1 = [40, 10, 90, 20, 110, 80]
tree1 = None
for i in arvore1:
    tree1 = insere(tree1, TreeNode(i))

imprimeArvore(tree1)

arvore2 = [40, 10, 90, 20, 110, 80,30]
tree2 = None
for i in arvore2:
    tree2 = insere(tree2, TreeNode(i))
imprimeArvore(tree2)

print(verifyStructure(tree1, tree2))
