sexo = str(input('Informe seu sexo: [M/F]')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Opção invalida, digite seu sexo: ')).strip().upper()[0]
print('Sexo registrado {} com sucesso'.format(sexo))