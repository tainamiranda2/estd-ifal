#receber uma string e mostrar a última palavra
def ver():

  nome=str(input("Digite seu nome?")).strip();
  saber=nome.split();

  print('Seu último nome é {}'.format(saber[len(saber)-1]));

ver();