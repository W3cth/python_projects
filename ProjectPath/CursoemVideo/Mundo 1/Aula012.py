nome = str(input('Digite seu nome: '))
if nome == 'Larry':
    print('Que nome bonito vc tem!! ')
elif nome == 'Bruno' or nome== 'João' or nome== 'Pedro':
    print('Seu nome é bem comum no Brasil! ')
else:
    print('Que nome comum vc tem! ')
print('Tenha um bom dia, {}!'.format(nome))