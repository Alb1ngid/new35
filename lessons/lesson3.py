# инкапсуляция
# 3 публичный защищенный-protected private-приватный
class Bank:
    def __init__(self, name, money, password):

        self.name = name
        self._money = money
        self.__passw = password

    def printn(self):
        print(self.name, self._money)

    def set_passw(self, paww):
        if len(self.__passw) > 6:
             self.__passw = paww
        else:
            print('')
        # raise ValueError



    def get_sawe(self):
        print(self.__passw)



b = Bank('beka', 0, '234ewsdt543ewdf')
b.set_passw('wertghytrfgyt')
b.get_sawe()
b.printn()
b._money = 100000000000

b._Bank__passw = 0
b.printn()

print(dir(b))



class Чайник:
    def __init__(self,name):
        self.name=name

    def кнопка(self):
        print('кипятить чайнить')
        self.__нагрев()
        self.__пластина()

    def __нагрев(self):
        print('start')

    def __выкл(self):
        print('выкл')

    def __пластина(self):
        self.__выкл()
        print('нагрев ')


a=Чайник('эмирлан')
a.кнопка()

#gitclone