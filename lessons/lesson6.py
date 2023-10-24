from art import tprint
import colorama


class A:
    name = True

    def __init__(self, nameTrue):
        self.nameTrue = nameTrue

    def print(self):
        return tprint(self.nameTrue)

    def colo(self):
        print(colorama.Back.BLACK)

    def colo2(self):
        print(colorama.Fore.BLUE)


a = A('Beka')
a.print()
a.colo2()
a.colo()
a.print()


# принципы наследование полиморфизм инкапсуляция
# __private _protected

# _Class__self

class B(A):
    def colo(self):
        print(colorama.Back.RESET)


class B2(object):
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    @property
    def name(self):
        print(self.__a, self.__b)

    @name.setter
    def name(self, a, d):
        self.__b = d
        self.__a = a


# print(dir(B2))
b = B2('name', '123')
b.name
b.name
b.name
print(dir(b))
print(B.mro())
