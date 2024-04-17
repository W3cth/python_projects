'''Randomização'''
import random
n1 = str(input('Digite o primeiro filme: '))
n2 = str(input('Digite o segundo filme: '))
n3 = str(input('Digite o terceiro filme: '))
lista = [n1,n2,n3]
escolhido = random.choice(lista)
print('O filme escolhido foi {} '.format(escolhido))

