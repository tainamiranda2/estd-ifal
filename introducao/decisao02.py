num1=int(input("Digite um número?"));

num2=int(input("Digite um número?"));

num3=int(input("Digite um número?"));

if num1 > num2 and num1 > num3:
  print("Num1,é maior", num1);

elif num2 > num1 and num2 > num3:
    print("Num2,é maior", num2)
elif num3 > num1 and num3 > num2:
    print("Num3,é maior", num3)

else:
      print("Tem erro")