from Piramide import *

n = 0
nPedrasDefeito = 0
pedrasDefeituosas = {}

def lerArquivo(arqNome, pedrasDefeituosas):
    print(">> Lendo arquivo ...")
    try:
        arquivo = open(arqNome, "r")
        #tokenize.
        n =  int(arquivo.readline().strip("\n"))
        nPedrasDefeito = arquivo.readline()

        linha = arquivo.readline()

        while (linha):
            split = linha.split(" ")
            pedrasDefeituosas[int(split[0])] = int(split[1].strip("\n"))
            linha = arquivo.readline()

        arquivo.close()
        print(">> Valor lido, estrutura de dados criada!")
    except FileNotFoundError:
        print("** Error: Arquivo não existe **")

    return n

if __name__ == "__main__": 
    n = 0
    nPedrasDefeito = 0
    pedrasDefeituosas = {}

    n = lerArquivo("./code/EP2/Entrada2.txt", pedrasDefeituosas)

    print(f">> Quantidade de pedras na base da pirâmide: {n}")
    print(f">> Lista de pedras defeituosas: {pedrasDefeituosas}")

    possibilidades = clibingPyramid(n, pedrasDefeituosas)
    print(f">>>>>Número de possibilidades diferentes: {possibilidades}")
    


