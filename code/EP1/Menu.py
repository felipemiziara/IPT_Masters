class Menu:
    def __init__(self,*args):
        self.opcioes = args

    def showMenu(self):
        for o in self.opcioes:
            print (str(o.opc) + " - " + str(o.texto))

    def execSelection(self, opc):
        if(opc>=0):
            self.opcioes[opc-1].func()

class MenuItem:
    def __init__(self, opc, texto, func=None):
        self.opc = opc
        self.texto = texto
        self.func = func

