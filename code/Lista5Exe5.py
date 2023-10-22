
         
pilha1 = []
pilha2 = []


def empilhar(p, elemento):
    p.append(elemento)

def desempilhar(p):
    if ( p ):
        return p.pop()
    else:
        return None

def enfileirar(elemento):
    empilhar(pilha1, elemento)


def desenfileirar():
    if(not pilha2):
        while (pilha1 ):
            empilhar(pilha2, desempilhar(pilha1))
    return desempilhar(pilha2)

enfileirar(1)
enfileirar(5)
enfileirar(8)
print(pilha1, end=",")
print (desenfileirar())
print (desenfileirar())
enfileirar(9)

print(pilha1, end=",")
print (desenfileirar())
print (desenfileirar())