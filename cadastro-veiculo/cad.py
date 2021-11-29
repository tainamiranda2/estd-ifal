#Cadastro de veiculos TAD(inserir, remover, consultar)
Menu=0
while Menu !=4:

  print('''[1]Cadastrar
[2] Consultar
[3] Remover
[4] Sair''')

  Menu=int(input("Escolha qual opção deseja seguir?"))

  if Menu == 1:
    Cadastro=[]
Veiculos=input("Digite uma marca de carro:")
Cadastro.append(Veiculos)
print(Cadastro)

while Veiculos!= '':

Veiculos=input("Digite uma marca de carro:")
Cadastro.append(Veiculos)
print(Cadastro)


   elif Menu == 2:
       Cadastro=[]
Veiculos=input("Digite uma marca de carro:")
Cadastro.append(Veiculos)
print(Cadastro)

while Veiculos!= '':

    Veiculos=input("Digite uma marca de carro:")
    Cadastro.append(Veiculos)
    print(Cadastro)

  elif Menu == 3:
      Cadastro=[]
Veiculos=input("Digite uma marca de carro para:")
Cadastro.remove(Veiculos)
print(Cadastro)

while Veiculos!= '':

    Veiculos=input("Digite uma marca de carro:")
    Cadastro.append(Veiculos)
    print(Cadastro)

  elif Menu == 4:
      Cadastro=[]
Veiculos=input("Digite uma marca de carro:")
Cadastro.append(Veiculos)
print(Cadastro)

while Veiculos!= '':

    Veiculos=input("Digite uma marca de carro:")
    Cadastro.append(Veiculos)
    print(Cadastro)

  else:
   print("Erro")
print("Fim do programa.")
#inserir