#construir um projeto que vai colorir uma matriz

#matriz 3x3
from termcolor import colored
    def colorir_regiao():
matriz = [
  [0, 0, 0],
 [0, 0, 0],
 [0, 0, 0],
 ]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um valor[{l}, {c}]: "))

print('-=' * 30)

for l in range(0, 3):
   for c in range(0, 3):
        print(f' [{matriz[l][c]}]', end=''  )
      
#print('\33[4;30;44m +matriz+ \33[m')

print("----fim-----matriz-------colorida ")
print(colored(matriz, 'blue'))


#colorir_regiao()