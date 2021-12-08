#empilhar, desempilhar e excluir
class Pilha():

  def __init__(self):
    self.items=[]

  def vazia(self):
    return self.items==[]

  def topo(self):
    return self.items[len(self.items)-1]

  def tamanho(self):
    return len(self.items)

  def empilhar(self,e):
    self.items.append(e)
    
  def desempilhar(self):
    return self.items.pop()