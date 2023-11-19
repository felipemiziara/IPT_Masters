class Tasks:
    def __init__(self, name, s, f):
        self.name = name
        self.s = s
        self.f = f

    def __repr__(self):
        return str(self.name)+ "[" + str(self.s) + "," + str(self.f) +"]"
    def __str__(self):
        return str(self.name)+ "[" + str(self.s) + "," + str(self.f) +"]"

def keyOdering(t):
    return t.f

def gulosoAtividade(tempos):
    solucao = []
    #Ordena pelo tempo final
    #O(nlogn)
    tempos.sort(reverse=False, key=lambda x: x.f)
    ultimoTempo = -1
    cont = 0
    #O(n)
    for t in tempos:
        if(t.s > ultimoTempo):
            solucao.append(t)
            ultimoTempo = t.f
    return solucao


def main():
    #s = [1, 3, 0, 5, 8, 5]
    #f = [2, 4, 6, 7, 9, 9]

    t1 = Tasks('A', 1, 2)
    t2 = Tasks ('B', 3,4)
    t3 = Tasks ('C', 0,6)
    t4 = Tasks ('D', 5,7)
    t5 = Tasks ('B', 8,9)
    t6 = Tasks ('B', 5,9)

    t = []
    t.append(t4)
    t.append(t5)
    t.append(t6)    
    t.append(t1)
    t.append(t2)
    t.append(t3)


    print(gulosoAtividade(t))
if __name__ == "__main__":
    main()
