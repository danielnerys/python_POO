class Passaro:
    def voar(self):
        print('Passaro pode voar')


class Pardal(Passaro):
    def voar(self):
        print('Pardal pode voar')


class Avestruz(Passaro):
    def voar(self):
        print('Avestruz não pode voar')

# ambas classes Pardal e Avestruz compartilham o mesmo metodo que é voar,

# no plano_voo, podemos receber o obj com o metodo, pois o metodo é polimorfo e tem valores diferentes para cada classe


def plano_voo(obj):
    obj.voar()


plano_voo(Pardal())
plano_voo(Avestruz())
