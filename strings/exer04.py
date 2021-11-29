#receber uma string e botar a ultima palavra junto a primeira
def ver():

  nome=str(input("Digite seu nome?")).strip();
  saber=nome.split();

  
  print('Seja bem vindo {}'.format(saber[len(saber)-1]));

ver();
#carlos drumonn 