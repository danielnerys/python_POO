class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    # Método de classe recebe parametro que aponta para a classe, pode acessar e modificar a classe

    @classmethod
    def criar_de_nascimento(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return cls(nome, idade)

  # Não recebe parametro, não pode acessar ou modificar a classe, apenas para realizar validações e verificaçãoes
    @staticmethod
    def maior_idade(idade):
        verificaçao = 'é maior de idade' if idade >= 18 else 'Não é maior'
        maior_idade = verificaçao
        return maior_idade

    def __str__(self):
        return f'Nome {self.nome} Idade: {self.idade}'


# instanciando a classe
p = Pessoa.criar_de_nascimento(1996, 9, 6, 'Daniel')

print(p)
print(p.nome, p.idade)
print(Pessoa.maior_idade(13))
print(Pessoa.maior_idade(19))
