"""Sortear ordem da lista"""
import random
n1 = str(input('Digite o primeiro nome: '))
n2 = str(input('Digite o segundo nome: '))
n3 = str(input('Digite o terceiro nome: '))
lista = [n1,n2,n3]
random.shuffle(lista)
print('A ordem dos alunos que irá apresentar o trabalho é {} '.format(lista))

