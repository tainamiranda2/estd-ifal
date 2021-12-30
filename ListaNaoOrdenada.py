castas=([9])

class ListaNaoOrdenada:
  def __init__(self): #construtor
   self.head = None
  def is_empty(self): 
   return self.head == None
minha_lista =ListaNaoOrdenada() 
minha_lista.is_empty()
