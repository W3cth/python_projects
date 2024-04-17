from datetime import date
ano = int(input('Qual o ano de seu nascimento? '))
atual = date.today().year
idade = atual - ano

if idade <= 9:
    print('Você tem {} anos e é Mirim'.format(idade))
elif idade <= 14:
    print('Você tem {} anos e é Infantil'.format(idade))
elif idade <= 19:
    print('Você tem {} anos e é Junior'.format(idade))
elif idade <= 25:
    print('Você tem {} anos e é Senior'.format(idade))
elif idade > 25:
    print('Você tem {} anos e é Master'.format(idade))