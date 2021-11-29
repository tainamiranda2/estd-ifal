nota1=int(input("Digite uma nota."));

nota2=int(input("Digite uma segunda nota."));

media=(nota1+nota2)/2

if media  >= 10:
  print("Aprovado com distinção")
elif media >= 7:
    print("Aprovado");
  
else:
  print("Reprovado")
  print("Fim do programa");