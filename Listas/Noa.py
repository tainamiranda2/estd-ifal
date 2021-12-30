class Noa:
    def __init__(self,valor_ini):
        self._dados = valor_ini
        self._proximo = None
    def getData(self):
        return self._dados
    def getNext(self):
        return self._proximo
    def setData(self, novo_valor):
        self._dados =  novo_valor
    def setNext(self, novo_proximo):
        self._proximo = novo_proximo
    def __str__(self):
      return f"[dados:{self._dados}|proximo:{self._proximo}]"