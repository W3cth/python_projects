'''Hipotenusa'''
import math
co= float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: ' ))
hi = math.hypot (co, ca)
print('A hipotenusa é do cateto oposto {} e do adjacente {} é de {:.2f}'.format(co, ca, hi))