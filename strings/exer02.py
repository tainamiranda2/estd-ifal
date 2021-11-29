#contando palavras
#função que conta quantas palavras tem no texto
#tem erro
import re;
def verificar():
  texto =input("Digite um texto?");

  resultado = len(re.findall(texto))

  print("Essas são as" +str(resultado)+"palvras");



verificar()