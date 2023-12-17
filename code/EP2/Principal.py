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
    except FileNotFoundError as erro:
        print(f"** Error: Arquivo não existe ** Error: {erro}")
        return 0

    return n

def verificaEntradas(niveis, qtdPedras, pedrasDefeituosas):
    if(niveis < 1 or niveis > 1000):
        print("+++++ ERROR: O número de níveis não suportado")
        return False
    if(qtdPedras < 0 or qtdPedras > (niveis*(niveis+1))/2):
        print("+++++ ERROR: O número de pedras defeituosas não suportado")
        return False
    for p in pedrasDefeituosas:
        if p < 1 or p > niveis:
            print("+++++ ERROR: O nivel da pedra defeituosa não é suportado.")
            return False
        if pedrasDefeituosas[p] < 1 or pedrasDefeituosas[p] > (niveis - (p-1)):
            print("+++++ ERROR: A posição da pedra defeituosa não existe.")
            return False
    return True

if __name__ == "__main__": 
    n = 0
    nPedrasDefeito = 0
    pedrasDefeituosas = {}

    n = lerArquivo("./code/EP2/Entrada2.txt", pedrasDefeituosas)

    print(f">> Quantidade de pedras na base da pirâmide: {n}")
    print(f">> Lista de pedras defeituosas: {pedrasDefeituosas}")

    if verificaEntradas(n, len(pedrasDefeituosas), pedrasDefeituosas):
        possibilidades = clibingPyramid(n, pedrasDefeituosas)
        print(f">>>>>Número de possibilidades diferentes: {possibilidades}")