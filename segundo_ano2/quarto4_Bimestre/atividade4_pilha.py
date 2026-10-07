class pilha:
    #construtor
    def __init__(self):
        self.dados = []

    #insserindo elementos na pilha
    def emplilhar(self,item):
        self.dados.append(item)

    #removendo da pilha
    def desempilhar (self):
        self.dados.pop(-1)