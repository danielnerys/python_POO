class Cachorro:
    # metodo construtor da classe
    # esse codigo será executado sempre que a classe for chamada
    def __init__(self, nome, cor, raca):
        print('Inicializando a classe')
        self.nome = nome
        self.cor = cor
        self.raca = raca

    # destrutor, exetuca sempre ao vim do codigo
    def __del__(self):
        print('Removendo a instancia da classe')

    def falar(self):
        print('auauau')


def criar_cachorro():
    c = Cachorro('Zeus', 'Preto', 'Pit-bull')
    print(c.nome)


c = Cachorro('Chappe', 'Amarelo', 'Vira-lata')
c.falar()
del c
criar_cachorro()
