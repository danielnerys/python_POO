class Foo:
    def __init__(self, x=None):
        self._x = x

    # o x age como um getter  e setter
    # retornando o valor de _x sem acessa-la diretamente assim preservando o valor 
    @property
    def x(self):
        return self._x or 0

    @x.setter
    def x(self, value):
        self._x += value

    @x.deleter
    def x(self):
        self._x = 0


foo = Foo(10)
print(foo.x)
del foo.x
print(foo.x)
foo.x = 1000
print(foo.x)
