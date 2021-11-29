#ver se uma palavra é polidoma

#def verificar():
  
palavra=input("Digite uma palavra para saber se é palindroma?")
if str(palavra) == str (palavra) [::-1]:
    print("Correto, palindrome")

else:
    print("Incorrento, não é palindrome")

#verificar()