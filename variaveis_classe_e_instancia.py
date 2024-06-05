# nesse arquivo tem um exemplo de uma variavel de classe e variavel na instancia
class Estudante:
    # escola é uma variavel de Classe, todos objetos criados apartir desse objeto, terão a variavel escola definida apartir dela
    escola = 'Dio'

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f'{self.nome} - {self.matricula} - {self.escola}'


def mostra_classe(*objetos):
    for obj in objetos:
        print(obj)


# na instancia de estudante01 ele tem a variavel escola igual a que foi definida na classe
estudante01 = Estudante('Daniel', '123')
estudante02 = Estudante('Amanda', '456')
print(estudante01, estudante02)


# apartir daqui, a variavel escola, foi alterada na instancia, apenas para o estudante 01
estudante01.escola = 'Python'
print(estudante01, estudante02)

# apartir daqui, estamos alterando a variavel de classe 'escola' para todos obj criador apartir da classe Estudante
Estudante.escola = 'Java'

print(estudante01, estudante02)

mostra_classe(estudante01, estudante02)
