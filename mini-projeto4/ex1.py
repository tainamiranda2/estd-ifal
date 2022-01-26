uma_lista = [9,8,7,3,4, 12, 80,2,1]

def ordenacao(verificar):
  if len(uma_lista)< 32:

    selectionSort(uma_lista)
    print("selectionSort", uma_lista)
  else:
    mergeSort(uma_lista)
print("megasort",uma_lista)


def selectionSort(lista):

     for index in range (0, len(uma_lista)):
       min_index=index

       for right in range(index + 1, len(uma_lista)):
         if uma_lista[right] < uma_lista[min_index]:
           min_index=right

       uma_lista[index], uma_lista[min_index] = uma_lista[min_index], uma_lista[index]
 

#selectionSort(uma_lista)
#print("selectionSort", uma_lista)

def mergeSort(uma_lista):

    if len(uma_lista) > 1:
        mid = len(uma_lista) // 2
        left = uma_lista[:mid]
        right = uma_lista[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              # The value from the left half has been used
              uma_lista[k] = left[i]
              # Move the iterator forward
              i += 1
            else:
                uma_lista[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            uma_lista[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            uma_lista[k]=right[j]
            j += 1
            k += 1

