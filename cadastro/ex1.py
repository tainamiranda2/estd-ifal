
class Veiculo:
	def __init__(self, placa, marca, modelo, ano, cod):
		self.placa = placa
		self.marca = marca
		self.modelo = modelo
		self.ano = ano
		self.cod = cod
	def imprimeVeiculo(self):
		return f"Placa: {self.placa}, Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Código: {self.cod}."
	def imprimeFinalPlaca(self):
		return self.placa[-1]
primeiro_veiculo = Veiculo('ASB4232', 'Toyota', 'AB-1', 2018, 41455)
segundo_veiculo = Veiculo('TTB3141', 'Honda', 'GX-1', 2017, 12145)
lista_veiculos = []

def cadastrarVeiculo(veiculo):
def cadastraVeiculo(veiculo):
	lista_veiculos.append(veiculo)
	print(f"Veículo de placa: {veiculo.placa} cadastrado")

def removerVeiculo(placa):
def removeVeiculo(placa):
	if len(lista_veiculos) != 0:
		for x in lista_veiculos:
			if x.placa == placa:
				lista_veiculos.remove(x)
	print(f'Veículo de placa: {placa} removido')

def consultaVeiculo(placa):
	if len(lista_veiculos) != 0:
		for x in lista_veiculos:
			if x.placa == placa:
				print(f'Placa: {x.placa}, Marca: {x.marca}, Modelo: {x.modelo}, Ano: {x.ano}, Código: {x.cod}')

print(primeiro_veiculo.imprimeVeiculo())
print(primeiro_veiculo.imprimeFinalPlaca())

print(segundo_veiculo.imprimeVeiculo())
print(segundo_veiculo.imprimeFinalPlaca())
cadastrarVeiculo(primeiro_veiculo)
cadastrarVeiculo(segundo_veiculo)
cadastraVeiculo(primeiro_veiculo)
cadastraVeiculo(segundo_veiculo)
print(len(lista_veiculos))
removerVeiculo("ASB4232")
removeVeiculo("TTB3141")
print(len(lista_veiculos))
consultaVeiculo("ASB4232")