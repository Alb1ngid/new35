# принципы ооп
#наследование-полиморфизм  инкапсуляция

# object
class A(object):  #суперкласс:родительский класс
    b = True

    def __init__(self, name):
        self.name = name

    def sNAME(self):
        print(self.name)


a = A('Бека')
a1 = A('Бека')
a2 = A('Бека')
a3 = A('Бека')
a4 = A('Бека')
a5 = A('Бека')
a6 = A('Бека')

a.sNAME()


class B(A): # дочерний класс
    b = False

    def __init__(self, name, age):
        super().__init__(name)
        # A.__init__(self,name)
        self.age = age

    def newName(self, name):
        self.name = name

    def sNAME(self):
        print(self.name, self.age)

    def NAME_NAME(self):
        A.sNAME(self)


b = B('name', 11)
b.sNAME()

b.newName('name2')
b.sNAME()
b.NAME_NAME()
# gitignore

print(B.mro())