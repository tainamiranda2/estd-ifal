#funcao recusiva para inverter palavras 
def inverter(palavra): 
    if len(palavra) == 0: 
        return palavra 
    else: 
        return inverter(palavra[1:]) + palavra[0] 
  
inversao = input("Dgite seu nome?")
  
print ("A palavra é: ",end="") 
print (inversao) 
  
print ("A palavra revertida: ",end="") 
print (inverter(inversao))  