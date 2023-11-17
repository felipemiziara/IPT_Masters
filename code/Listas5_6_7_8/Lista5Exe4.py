class Lista5Exec4:
 
    def __init__(self, capacity):
        self.pos = -1
        self.capacity = capacity

        self.pilha = []
        self.result = []

        self.pri = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def vazio(self):
        if self.pos == -1:
            return True
        else:
            return False
        
    def verTopo(self):
        return self.pilha[self.pos -1]
    
    def empilhar(self, elemento):
        self.pilha.append(elemento)
        self.pos+=1

    def desempilhar(self):
        if ( not self.vazio()):
            self.pos-=1
            return self.pilha.pop()
        else:
            return None
        
    def eLetra(self, ele):
        return ele.isalpha()
    
    def prioridade(self, op1):
        try:
            if(self.pri[op1] <= self.pri[self.verTopo()]):
                return True
            else:
                return False
        except KeyError:
            return False
    
    def converter(self, input):
        for i in input:
            print(i)
            if(self.eLetra(i)):
                self.result.append(i)
            elif(i == '('):
                self.empilhar(i)
            elif(i == ')'):
                while ((not self.vazio()) and (self.verTopo() != '(')):
                    ele = self.desempilhar()
                    self.result.append(ele)
                if not self.vazio() and self.verTopo() != '(':
                    return -1
                else:
                    self.desempilhar()
            else:
                while (not self.vazio()) and (self.prioridade(i)):
                    self.result.append(self.desempilhar())
                self.empilhar(i)
        while (not self.vazio()):
            self.result.append(self.desempilhar())
        
        for j in self.result:
            print(j, end="")

                

if __name__ == '__main__':
        exp = "a+b*(c^d-e)^(f+g*h)-i"
        obj = Lista5Exec4(len(exp))
        obj.converter(exp)



#lista = Lista5Exec4()
#lista.converter("a+b*(c^d-e)^(f+g*h)-i")
#print(lista.operador)

#           abcd^e-fg+h*(*+i-
# Correto:  abcd^e-fgh*+^*+i-