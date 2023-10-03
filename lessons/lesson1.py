# ООП
# Классы

a = 'str',1, 1.00,True,[],{},()
print(type(a))


def a(x,y):
    print(x+y)

a(2,6)

class Human:
    head=1
    # свойства-переменная внутри класса
    # магические методы __name__
    def __init__(self, name,age): # конструктор класса
        self.name=name
        self.age=age

    def __str__(self):
        return f"name is {self.name}\n" \
               f"age is {self.age} \n" \
               f"head:{self.head}\n"
    # методы - функция def внутри класса
    def printHead(self):
        print(self.name,'is student')


human=Human('beka',20) # экземпляры класса
human2=Human('Бермет0', 30)
human3=Human('Бермет1', 30)
human33=Human('Бермет3', 30)

human33.printHead()
human3.printHead()
print(human)
print(human2)
print(human3)
print(human33)