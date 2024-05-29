# Criando classe
class Bicicleta:
    # definindo atributos da classe
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    # definindo metodos da classe
    def troca_cor(self, cor):
        self.cor = cor

    def buzinar(self):
        print('plim plim...')

    def parar(self):
        print('Parando bicicleta..')
        print('Bicicleta parada!')

    def correr(self):
        print('Vrumm')

    def __str__(self):
        return f"{self.__class__.__name__}:{','.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


b1 = Bicicleta('Vermelha', 'Caloi', 2022, 1999)
b1.correr()
b1.parar()
b1.troca_cor('azul')
print(b1)
