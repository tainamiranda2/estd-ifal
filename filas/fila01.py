class Fila:
    #inicia vazia
    def __init__(self):
        self.fila = []
        #colocar algo
    def inseri(self, n):
        self.fila.append(n)
        #excluir primeiro elementpo
    def excluir(self):
        if not self.vazia():
            del self.fila[0]

        #ver tamho
    def tamanho(self):
        return len(self.fila)

    def vazia(self):
        return self.tamanho() == 0


fila = Fila()
print(fila.vazia)
class Fila:
    #inicia vazia
    def __init__(self):
        self.fila = []
        #colocar algo
    def inseri(self, n):
        self.fila.append(n)
        #excluir primeiro elementpo
    def excluir(self):
        if not self.vazia():
            del self.fila[0]

        #ver tamho
    def tamanho(self):
        return len(self.fila)

    def vazia(self):
        return self.tamanho() == 0


fila = Fila()
print(fila.vazia)
