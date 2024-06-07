# importar modulo ABC (ABSTRACT METHOD CLASSSES)
from abc import ABC, abstractmethod

#definindo controle remoto como uma classe abstrata, onde seus metodos servem de base para outras classes
class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractmethod
    def marca(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print('Ligando a TV...')
        print('Ligada!')

    def desligar(self):
        print('Desligando a TV...')
        print('Desligada')

    @property
    def marca(self):
        return ('LG')


class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print('Ligando ar condicioando...')
        print('Ligado!')

    def desligar(self):
        print('Desligando ar condicionado...')
        print('Desligado')

    @property
    def marca(self):
        return ('Elgin')


controle = ControleTV()
controle.ligar()
print(controle.marca)

ar_condicionado = ControleArCondicionado()
ar_condicionado.ligar()
print(ar_condicionado.marca)
