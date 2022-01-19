
def mergeSort(uma_lista):
  print("Splitting ",uma_lista)
  if len(uma_lista)>1:
    meio = len(uma_lista)//2
    esquerda = uma_lista[:meio]
    direita = uma_lista[meio:]
    mergeSort(esquerda)
    mergeSort(direita)
## aqui vai o merge. ver próximo slide.
  print("Merging ",uma_lista)
uma_lista = [54,26,93,17,77,31,44,55,20, 
 1,2,3,4,5,6,7,8,9,10, 
 14, 13,14,15,16,17,18,99,100,
  101,102,103, 300 ]
mergeSort(uma_lista)
print(uma_lista)

def mergeSort(uma_lista):
#...
  i=0
  j=0
  k=0
  while i < len(esquerda) and j < len(direita):
    if esquerda[i] < direita[j]:
      uma_lista[k]=esquerda[i]
      i=i+1
    else:
      uma_lista[k]=direita[j]
      j=j+1
      k=k+1
  while i < len(esquerda):
      uma_lista[k]=esquerda[i]
      i=i+1
      k=k+1
  while j < len(direita):
      uma_lista[k]=direita[j]
      j=j+1
      k=k+1
print("Merging ",uma_lista)