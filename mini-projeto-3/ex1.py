
class HashTable:
  def __init__(self):
    self._tamanho = 200 #
    self._slots = [None] * self._tamanho
    self._valores = [None] * self._tamanho

  def hashfunction(self, chave, tamanho):
      sum = 0      
      for pos in range(len(chave)):
          sum = sum+ord(chave[pos])*(pos+1)
      return sum%tamanho


  def rehash(self,oldhash,tamanho):
    return (oldhash+1)%tamanho

  def put(self,chave,valor):
    valor_hash = self.hashfunction(chave,len(self._slots))

    if self._slots[valor_hash] == None:
        self._slots[valor_hash] = chave
        self._valores[valor_hash] = valor
    else:
      if self._slots[valor_hash] == chave:
       self._valores[valor_hash] = valor #replace
      else:
        proximo_slot = self.rehash(valor_hash,len(self._slots))
        while self._slots[proximo_slot] != None and \
        self._slots  [proximo_slot] != chave:

         proximo_slot = self.rehash(proximo_slot,len(self._slots))
        if self._slots[proximo_slot] == None:
          self._slots[proximo_slot]=chave
          self._valoresvg[proximo_slot]=valor
        else:
            self._valores[proximo_slot] = valor #replace

  def get(self,chave):
    slot_inicial = self.hashfunction(chave,len(self._slots))
    valor = None
    parar = False
    encontrou = False
    posicao = slot_inicial
    while self._slots[posicao] != None and \
        not encontrou and not parar:
      if self._slots[posicao] == chave:
        encontrou = True
        valor = self._valores[posicao]
      else:
        posicao=self.rehash(posicao,len(self._slots))
        if posicao == slot_inicial:
            parar = True
    return posicao

  def __getitem__(self,chave):
    return self.get(chave)
  def __setitem__(self,chave,valor):
    self.put(chave,valor)


Estacionamento = HashTable()

def Inserir():
	pl=input('placa do veículo: ').upper() 
	mod = input('Informacoes do veiculo: ')
	Estacionamento.put(pl,mod) 

def PosicaoVeic():
    placa=input('buscar veiculo. insira placa: ').upper()
    if placa in Estacionamento._slots: 
        pos = Estacionamento.get(placa) 
        print(f'Vaga do veiculo: {pos}') 
    else:
        print('Veículo não encontrado')

def RetirarVeic():
    placa=input('placa do veículo: ').upper()
    if placa in Estacionamento._slots:
        pos = Estacionamento.get(placa)
        del Estacionamento._slots[pos]  
        del Estacionamento._valores[pos] 


Inserir()
PosicaoVeic()

    