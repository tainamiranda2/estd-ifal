#funcao recursiva para encontrar palavra palindroma
def palindroma():
  imprime()

  palavra=input("Digite uma palavra para saber se é palindroma?")

    if str(palavra) == str (palavra) [::-1]:
    print("Correto, palindrome")

    else:
    print("Incorrento, não é palindrome")

def imprime():
  print("ola, funcao recursiva2")

palindroma()


