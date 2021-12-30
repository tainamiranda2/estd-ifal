from Noa import *
class Lista_Nao_ordenada:

  def _init_(self):
    self.head =None
    self.tam=0
  
  def is_empty(self):
    return self.head== None

  def add(self, item):
    #teste para ver se pega
    temp = Noa(item)
    temp.setNext(self.head)
    self.head = temp
    self.tamanho+=1


  def size (self):
    return self.tamanho