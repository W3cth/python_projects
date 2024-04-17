soma = 0
cont = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        soma = soma + c
        cont = cont + 1
print('Os total dos valores solicitados é {} e soma de todos os valores é {}'.format(cont, soma))