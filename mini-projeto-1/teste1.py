from collections import deque
from termcolor import colored

 # def fila(dequ):
# Cria uma fila com três elementos.
def colorir_regiao(regiao1):
  
  regiao1 = deque ([1,0,0,2,2])

  print(colored(regiao1, 'blue'))
                  
  #print("Fila: ", regiao1)

  # Adiciona um elemento ao final da fila.
  regiao1.append(7)
  print("Adicionando um elemento: ", regiao1)

  # Remove o primeiro elemento adicionado à fila.
  regiao1.popleft()
  print("Removendo um elemento: ", regiao1)
  #print(colorir_regiao)