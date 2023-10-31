#
#
class A:
    a = 1  # свойства

    def __init__(self, a1, b2):
        self.a1 = a1
        self.b2 = b2

    def adb(self):
        print(self.a1, self.b2)

    def __str__(self):
        return f'{self.a1}, {self.b2},{self.a}'


a = A('a', 2)
# a.__str__()
# print(a)


class B(A):
    def __init__(self, a1, b2, d3='1'):
        super().__init__(a1, b2)
        self.d3 = d3

    def adb(self):
        print(self.a1,self.b2,self.d3)

    def c(self):
        # A.adb(self)
        self.adb()


p1 = B('a1', 'b2','7')
p1.c()

import random

# модули
# встроенные
# внутренние \ собвственные

# внешние модули
# venv -