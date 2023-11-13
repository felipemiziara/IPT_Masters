import sys
import time
import math
from Menu import *
from LinkedList import *

arquivo1 = None
arquivo2 = None
arquivo3 = None
lista1 = LinkedList()
lista2 = LinkedList()
lista3 = None

def gravaValor3Opc():
    global lista3
    if(lista3 is None):
        print(" ")
        print ("ERROR: Nenhuma operação foi executa ainda. Tente alguma operação com as opções 3 ou 4.")
        print(" ")
    else:
        arquivo3 = input("Entre com o nome do arquivo:")
        if(not arquivo3):
            print("** Erro, arquivo não selecionado **")
        else:
            print(">> Salvando arquivo ...")
            try:
                conteudo = lista3.imprimirNumero()
                arquivo = open(arquivo3, "w")
                arquivo.write(conteudo)
                arquivo.flush()
                arquivo.close()
                print(">> Valor salvo com sucesso!")
            except FileNotFoundError:
                print("** Error ao gravar o arquivo **")
    time.sleep(2)

def somaOpc():
    global lista3
    print(" ")
    print(">> A soma de valores: ")
    lista3 = soma(lista1.head, lista2.head)
    if (lista3):
        resultado = lista3.imprimirNumero()
    print(lista1.imprimirNumero() + " + " + lista2.imprimirNumero() + " = " + resultado)
    print(" ")
    time.sleep(2)


def multiplicacaoOpc():
    global lista3
    print(" ")
    print(">> O produto dos valores: ")
    lista3 = multiplicacao(lista1.head, lista2.head)
    if(lista3):
        resultado = lista3.imprimirNumero()
    print(lista1.imprimirNumero() + " x " + lista2.imprimirNumero() + " = " + resultado)
    print(" ")
    time.sleep(2)

def multiplicacao(cabeca1, cabeca2):
    listasSomas = []
    if(cabeca1 is None or cabeca2 is None):
        print ("ERROR: Os arquivos ainda não foram lidos, tente as opções 1 ou 2 antes de multiplicar.")
        print(" ")
        time.sleep(2)
    else:
        l1 = cabeca1
        cont = 0
        while(l1 is not None):
            num1 = 0
            num1 = int(l1.data)
            l1 = l1.prox
            l2 = cabeca2
            sobeNum = 0
            listaSoma = LinkedList()
            listasSomas.append(listaSoma)
            for i in range(0, cont):
                listaSoma.addFila(Node(0))
            while(l2 is not None):
                num2 = int(l2.data)
                l2 = l2.prox
                num = num1*num2 + sobeNum
                if(num >= 10):
                    sobeNum = math.floor(num/10)
                    num = num%10
                else:
                    sobeNum = 0
                listaSoma.addFila(Node(num))
            if(sobeNum):
                listaSoma.addFila(Node(sobeNum))
            cont +=1
        resultado = LinkedList()
        for obj in listasSomas:
            resultado = soma(resultado.head, obj.head)
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
    if(cabeca1 is None and cabeca2 is None):
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
    print(">> Lendo arquivo ...")
    try:
        arquivo = open(arqNome, "r")
        conteudo = arquivo.read()
        #Aqui eu vou ler o arquivo e construir a lista com prioridade de fila
        for c in conteudo:
            lista.addPilha(Node(c))
        #lista.imprimir()
        arquivo.close()
        print(">> Valor lido, estrutura de dados criada!")
    except FileNotFoundError:
        print("** Error: Arquivo não existe **")


def lerAqruivo1():
    global arquivo1
    print(" ")
    if(arquivo1):
        print(">> Arquivo já encontrado via parametro de execução: " + arquivo1)
    else:
        arquivo1 = input("Entre com o nome do arquivo:")
    lerArquivo(arquivo1, lista1)
    arquivo1 = None
    print(" ")
    time.sleep(2)


def lerArquivo2():
    global arquivo2
    print(" ")
    if(arquivo2):
        print(">> Arquivo já encontrado via parametro de execução: " + arquivo2)
    else:
        arquivo2 = input("Entre com o nome do arquivo:")
    lerArquivo(arquivo2, lista2)
    arquivo2 = None
    print(" ")
    time.sleep(2)

def main():
    global arquivo1
    global arquivo2 

    if(len(sys.argv) > 1): 
        arquivo1 = sys.argv[1]
    
    if(len(sys.argv) >2):
        arquivo2 = sys.argv[2]


    menuItem1 = MenuItem(1, "Ler o primeiro valor do arquivo (v1)", lerAqruivo1)
    menuItem2 = MenuItem(2, "Ler o segundo valor do arquivo (v2)", lerArquivo2)
    menuItem3 = MenuItem(3, "Somar V1 com V2 e gerar um terceiro valor (V3)", somaOpc)
    menuItem4 = MenuItem(4, "Multiplicar V1 por V2 e gerar um terceiro valor (V3)", multiplicacaoOpc)
    menuItem5 = MenuItem(5, "Salvar o resultado (V3) em um arquivo", gravaValor3Opc)
    menuItem6 = MenuItem(6, "Sair da calculadora", print)

    menu = Menu(menuItem1, menuItem2,menuItem3,menuItem4,menuItem5,menuItem6)
    opc = 0
    print(" ")
    print(" ")
    while opc != 6:
        menu.showMenu()
        opc = int(input("Digite sua opção: "))
        menu.execSelection(opc)
    return

if __name__ == "__main__":
    main()

