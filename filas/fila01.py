class Fila:
  #construtor
    #inicia vazia
    def __init__(self):
        self.fila =  [1,2,3]
       
        #colocar algo
    def inseri(self, n):
        self.fila.append(n)
        #excluir primeiro elemento
    def excluir(self):
        if not self.vazia():
           #remover do inicio
            del self.fila[0]

        #ver tamanho
    def tamanho(self):
        return len(self.fila)
#ver se esta vazia
    def vazia(self):
        return self.tamanho() == 0
fila = Fila()
print(fila.vazia)

 #def tamanho(regiao1):
      #return len(regiao1.matriz)

   #def vazia(regiao1):
    #  return regiao1.tamanho()==0