class Noh:
    def __init__(self, valor_inicial):
        self.dados = valor_inicial
        self.proximo = None

    def getData(self):
        return self.dados

    def getNext(self):
        return self.proximo

    def setData(self, novo_valor):
        self.dados = novo_valor

    def setNext(self, novo_proximo):
        self.proximo = novo_proximo

    def __str__(self):
        return f"[dados:{self.dados}|proximo:{self.proximo}]"


class Cartas:
    def __init__(self):
        self.cartas = None

    def adicionar(self, item):
        atual = self.cartas
        anterior = None
        parar = False

        while atual != None and not parar:
            if atual.getData() > item:
                parar = True
            else:
                anterior = atual
                atual = atual.getNext()

        temp = Noh(item)
        if anterior == None:
            temp.setNext(self.cartas)
            self.cartas = temp
        else:
            temp.setNext(atual)
            anterior.setNext(temp)

    def pesquisar(self, item):
        atual = self.cartas
        encontrou = False
        parar = False

        while atual != None and not encontrou and not parar:
            if atual.getData() == item:
                encontrou = True
            else:
                if atual.getData() > item:
                    parar = True
                else:
                    atual = atual.getNext()
        print(encontrou)

    def remover(self, item):
        atual = self.cartas
        anterior = None
        encontrou = False
        while atual != None and not encontrou:  #percorre a lista
            if atual.getData() == item:
                encontrou = True
            else:
                anterior = atual
                atual = atual.getNext()

        if anterior == None and encontrou:
            self.cartas = atual.getNext()
        elif encontrou:
            anterior.setNext(atual.getNext())

    def exibir(self):
        atual = self.cartas
        lista = []
        while atual != None:  #percorre a lista
            lista.append(atual.dados)
            atual = atual.getNext()
        print(lista)


#Menu=int(input("\n""1:Adicionar uma carta""\n""2:Remover uma carta""\n""3:Exibindo as cartas""\n""4:Verificar se tem uma carta""\n""Escolha uma opçaõ?")

#cartas.adicionar(['carta1', 'carta2', 'carta3'])

#print("Opção escolhida:",Menu)
cartas = Cartas()
#if Menu==3:
print("Cartas/baralho e naipes disponiveis:")
cartas.adicionar("Paus")
cartas.adicionar("Espadas")
cartas.adicionar("Copas")
cartas.adicionar("Ouros")
cartas.adicionar("carta1")
cartas.adicionar("carta2")
cartas.adicionar("carta3")
cartas.exibir()

#elif Menu==4:
print("Verificar se a carta tem disponivel:")
cartas.pesquisar('carta3')

#elif Menu==2:
print("Remover uam carta e ver o resulatdo:")
cartas.remover('carta2')

#elif Menu==1:
print("Exibindo as cartas")
cartas.exibir()
#else:
# print("Erro")
print("Fim do programa")
