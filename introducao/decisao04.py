lado1=int(input("Digite o primeiro lado?"))

lado2=int(input("Digite o segunda lado?"))

lado3=int(input("Digite o terceiro lado?"))

if lado1 == lado2 and lado1 == lado3:
  print("triangulo equilatero");
elif lado2 == lado1 or lado2 == lado3:
  print("triangulo isosceles");
elif lado1 != lado2 or lado2 != lado3:
  print("triangulo escaleno")
else:
    print("algo deu errada")
