def contarDegraus(qtdDegraus, memoizationTable):
 
    if (qtdDegraus <= 1):
        return 1
 
    if(memoizationTable[qtdDegraus] != -1):
        return memoizationTable[qtdDegraus]
 
    s = contarDegraus(qtdDegraus - 1, memoizationTable) + contarDegraus(qtdDegraus - 2, memoizationTable)
    memoizationTable[qtdDegraus] = s
    return memoizationTable[qtdDegraus]


def main():
    qtdDegraus = 5
    memoizationTable = [-1 for i in range(qtdDegraus+1)]
    resposta = contarDegraus(qtdDegraus, memoizationTable)
    print("")
    print(f"Número de possibilidades para {qtdDegraus} degraus é: {resposta}")
    print("")

if __name__ == "__main__":
    main()
