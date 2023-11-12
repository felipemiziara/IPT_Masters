import sys
import time
import math
from Menu import *
from LinkedList import *

arquivo1 = None
arquivo2 = None
lista1 = LinkedList()
lista2 = LinkedList()

def somaOpc():
    print("A soma de valores: ")
    lista = soma(lista1.head, lista2.head)
    lista.imprimirNumero()

def multiplicacaoOpc():
    print("O produto dos valores: ")
    lista = multiplicacao(lista1, lista2)
    #lista.imprimirNumero()

def multiplicacao(l1, l2):
    m1 = None
    m2 = None
    if(l1.size < l2.size):
        m1 = l1
        m2 = l2
    else:
        m1=l2
        m2=l1
    fator = converterLongInt(m1)
    #print(fator)
    resultado = LinkedList()
    cont = 0
    while cont < fator:
        resultado = soma(m2.head, resultado.head)
        cont +=1
    return resultado


def converterLongInt(lista):
    ele = None
    if(lista is not None):
        ele = lista.head
    cont = 0
    resultado = 0
    while ele:
        resultado += int(ele.data)*math.pow(10, cont)
        cont +=1
        ele = ele.prox
    return resultado

def soma(cabeca1, cabeca2):
    listaSoma = LinkedList()
    if(lista1.head is None or lista2.head is None):
        print ("ERROR: Os arquivos ainda não foram lidos, tente as opções 1 ou 2 antes de somar.")
        print(" ")
        time.sleep(2)
    else:
        l1 = cabeca1
        l2 = cabeca2
        sobUm = 0
        while(l1 is not None or l2 is not None):
            num1 = 0
            num2 = 0

            if(l1 is not None):
                num1 = int(l1.data)
                l1 = l1.prox
            if(l2 is not None):
                num2 = int(l2.data)
                l2 = l2.prox
            num = num1 + num2 + sobUm

            if(num >= 10):
                sobUm = 1
                num = num - 10
            else:
                sobUm = 0
            
            listaSoma.addFila(Node(num))
        if(sobUm):
            listaSoma.addFila(Node(1))
    return listaSoma

def lerArquivo(arqNome, lista):
    arquivo = open(arqNome, "r")
    conteudo = arquivo.read()
    #Aqui eu vou ler o arquivo e construir a lista com prioridade de fila
    for c in conteudo:
         lista.addPilha(Node(c))
    lista.imprimir()
    arquivo.close()

def lerAqruivo1():
    lerArquivo(arquivo1, lista1)

def lerArquivo2():
    lerArquivo(arquivo2, lista2)

def main():
    # Recebe um parâmetro via linha de comando
    global arquivo1 
    arquivo1 = sys.argv[1]
    global arquivo2 
    arquivo2 = sys.argv[2]


    menuItem1 = MenuItem(1, "Ler o primeiro valor do arquivo (v1)", lerAqruivo1)
    menuItem2 = MenuItem(2, "Ler o segundo valor do arquivo (v2)", lerArquivo2)
    menuItem3 = MenuItem(3, "Somar V1 com V2 e gerar um terceiro valor (V3)", somaOpc)
    menuItem4 = MenuItem(4, "Multiplicar V1 por V2 e gerar um terceiro valor (V3)", multiplicacaoOpc)
    menuItem5 = MenuItem(5, "Salvar o resultado (V3) em um arquivo", soma)
    menuItem6 = MenuItem(6, "Sair da calculadora", soma)

    menu = Menu(menuItem1, menuItem2,menuItem3,menuItem4,menuItem5,menuItem6)
    opc = 0
    while opc != 6:
        menu.showMenu()
        opc = int(input("Digite sua opção: "))
        menu.execSelection(opc)
    return

if __name__ == "__main__":
    main()

