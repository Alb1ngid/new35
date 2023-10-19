# venv
# ветки гит
# MRO
# 1
# class V:...
# class S:...
# class B(S):...
#
# class A(B,V):...
#
# print(A.mro())


# venv - тюрьма для зависимостей
# зависимости - библиотеки или фреймворки расширения

# модули
# 1 встроенные модули

import random

import math

print(math.pi)

from math import pi

print(pi)
# 2 собвственные модули

from lesson4 import Newclass

k = Newclass('beka', 20)
k.nameis = 'qwes'
k.nameis

from HomeWork import Hero
Hero.AirHero

#3 внешние модули
# venv

from art import tprint
import colorama
print(colorama.Back.BLACK)
print(colorama.Fore.BLUE)
tprint('HELLO WORLD')
print(colorama.Fore.RED)
tprint('ertghjiuyhjk')
print('ertghjkl')