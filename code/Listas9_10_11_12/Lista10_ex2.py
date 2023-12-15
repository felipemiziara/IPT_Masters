def contarMoedas(coins, troco):

    a = [[float("-inf") for j in range(troco + 1)] for i in range(len(coins) + 1)]
    for i in range(len(a)):
        a[i][0] = 0

    for i in range(1, len(a)):
        for j in range(1, len(a[0])):
            if coins[i - 1] > j:
                a[i][j] = a[i - 1][j]
            else:
                a[i][j] = max(a[i - 1][j], a[i][j - coins[i - 1]] + 1)
    return (a[-1][troco])

def main():
    coins = [3, 5]
    n = len(coins)
    troco = 50
    print("")
    print(f"Para este grupo de moedas {coins}, o máximo de moedas para um troco de {10} é: {contarMoedas(coins, troco)}")
    print("")

if __name__ == "__main__":
    main()
