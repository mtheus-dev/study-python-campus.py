class Fila:
    #condtrutor 
    def __init__(self):
        self.dados = []

    #adicionando na fila
    def inserir(self,item):
        self.dados.append(item)

    #removendo da fila
    def remover (self):
        self.dados.pop(0)