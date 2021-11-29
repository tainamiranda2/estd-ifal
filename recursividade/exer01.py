#criar uma funcao fatorial recursivo

def fatorial(num):
  if num == 0 or num ==1:
    return 1
  else:
    return num * fatorial(num -1)


res=int(input("Digite um numero para ver o fatorial?"));

x=fatorial(res)
print("O fatorial é de" , x,res)
