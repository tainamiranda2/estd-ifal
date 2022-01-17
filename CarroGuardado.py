#criei isso aqui mas ja coloquei tudo em main.py. pode apagar isso aqui depois


from main import *

#instanciar um map
Estacionamento = HashTable()

def Inserir():
	pl=input('Informe a placa do veículo: ') #recebe placa
	mod = input('Informe Modelo e Cor do Veículo: ')#recebe informacao do veiculo
	Estacionamento.put(pl,mod) #veiculo inserido

#função pra pegar posicao do veiculo. usando o metodo get que está em HashTable
def PosicaoVeic():
    placa=input('Informe a placa do veículo: ')
    if placa in Estacionamento._slots: 
        pos = Estacionamento.get(placa) #aqui pega a posicao e guarda em 'x'
        print(f'Vaga do veiculo: {pos}') #depois só printar
    else:
        print('Veículo não encontrado')

def RetirarVeic():
    placa=input('placa do veículo: ')#recebe a key (placa)
    if placa in Estacionamento._slots: #se a placa tiver lá em slots,pega a posicao dela e remove de slots e de valores.
        pos = Estacionamento.get(placa) #pega a posicao e guarda em x
        del Estacionamento._slots[pos]  # remove aqui
        del Estacionamento._valores[pos] # remove aqui tambem #ta resolvido!


