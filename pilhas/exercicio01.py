
#desenvolver uma função recusiva para  remover todos os elementos de uma pilha

class Pilha ():
# pilha1= ['leite','suco', 'açucar'];
  def __init__(self):
    self.items=[]
  
  def vazia(self):
    return self.items == []
  
  def topo(self):
    return self.items[len(self.items)]

  def tamanho(self):
    return len(self.items)

  def empilhar (self, e):
    return self.items.append(e)
  #excluir
  def desempilhar (self):
    return self.items.pop()
    
#desenvolver uma função recusiva para  remover todos os elementos de uma pilha
def frutas():
  pilha = ['banana', 'goiaba', 'manga', 'coco']
  print("A pilha: ", pilha)

  pilha.pop()
  print("A pilha com um ite´m removido: ", pilha)

frutas()