from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano de seu nascimento: '))
idade = atual - nasc
print('Quem nasceu em {}, tem {} anos em {}'.format(nasc, idade, atual))


if idade == 18:
    print('Você tem {} anos e precisa se alistar imediatamente!!!' .format(idade))
    
elif idade < 18:
    saldo = 18 - idade
    print('Você tem {} anos e ainda faltam {} anos para se alistar'.format(idade, saldo))


elif idade > 18:
    saldo = idade - 18
    print('Você tem {} anos e ja deveria ter se alistado há {} anos '.format(idade, saldo))