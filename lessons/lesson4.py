# classmetod staticmethod

class Name:

    def __init__(self, name, age):
        self.__age = age
        self.__name = name

    def printt(self):
        print(self.__age)

    @property
    def nameis(self):
        return (self.__name)

    @nameis.setter
    def nameis(self, name):
        self.__name = name

    @staticmethod
    def method():
        print('это статический метод')


name1 = Name('name', 18)
name1.nameis = 'wer'
print(name1.nameis)


class Person:

    # def __init__(self, age2):
    #     self.__age2 = age2

    # def printt(cls):
    #     print(cls.age,'это метод класса Person')

    @staticmethod
    def age1(age):
        if age > 18:
            print(True)
        else:
            print(False)

    @classmethod
    def classmethod(cls):
        print('это класс метод')


q = Person


# q.printt()


# Person.classmethod()


# a = Person(age=19)
# a.age1(a.age)
# Person.age1(a.age)
#
# Name.method()
#
# n = Name('18')
# n.method()
# Person.age1(n.age)

class Myclass():
    total_object = 0

    def __init__(self):
        Myclass.total_object = Myclass.total_object + 1

    @classmethod
    def total_OBJECT(cls):
        print('количество обьектов', cls.total_object)

#
# myobj = Myclass()
# myobj1 = Myclass()
# myobj2 = Myclass()
# myobj3 = Myclass()


# Myclass.total_OBJECT()


# множественное наследование

class Newclass(Person, Myclass, Name):  # дочерний класс

    def __init__(self, name, age):
        Name.__init__(self, name, age)
        self.age = age
        self.name = name

    def printt(self):
        print(self.age, 'это метод класса New')


# mro-method resolution order

print(Newclass.mro())

ob = Newclass('name', 19)

ob.printt()
Newclass.total_OBJECT()
ob.nameis='qq'
print(ob.nameis)
Newclass.age1(ob.age)


class A:...

class B(A):...

class C:...

class D(B,C,A):...

c=D