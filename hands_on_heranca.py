# herança simples
class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print('ligando motor..')

    def __str__(self):
        return f"{self.__class__.__name__}:{','.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Motocicleta(Veiculo):
    pass


class Carro(Veiculo):
    pass


class Caminhao(Veiculo):
    # ao definir um novo metodo inicializador, podemos herdar todas caracteristicas da classe pai
    def __init__(self, cor, placa, numero_rodas, carregado):
        # e colocar o metodo super para herdar os metodos e abaixo colocar os novos metodos
        super().__init__(cor, placa, numero_rodas)
        self.carregado = False

    def esta_carregado(self):
        print(f'{'sim' if self.carregado else 'Não'} estou carregado')


moto = Motocicleta('Preta', 'Abc-1234', 2)
moto.ligar_motor()

carro = Carro('Vermelho', 'xde-0031', 4)
carro.ligar_motor()

caminhao = Caminhao('Verde', 'rte-2130', 8, True)
caminhao.ligar_motor()
caminhao.esta_carregado()
print(caminhao)
