class ListaNaoOrdenada:
  def __init__(self): #construtor
    self.head = None
def is_empty(self): #<<<<
  return self.head == None
minha_lista = ListaNaoOrdenada() #exemplo de uso
minha_lista.is_empty()

def size(self):
  atual = self.head
  contador = 0
  while atual != None:
  contador = contador + 1
  atual = atual.getNext()
  return contador

def search(self,item):
atual = self.head #atual == temp
encontrou = False
while atual != None and not encontrou:
if atual.getData() == item:
encontrou = True
else:
atual = atual.getNext()
return encontrou

def remove(self,item):
atual = self.head
anterior = None
encontrou = False
while not encontrou: #percorre a lista
if atual.getData() == item:
encontrou = True
else:
anterior = atual
atual = atual.getNext()
if anterior == None:
self.head = atual.getNext()
else:
anterior.setNext(atual.getNext())