numero = int(input('Digite um número inteiro: '))
print ('''Escolha uma das bases de conversão: 
[1] BINÁRIO
[2] OCTAL
[3] HEXADECIMAL''')
op = int(input('Sua opção foi: '))

if op == 1:
    print('O número escolhido foi {} e a sua conversão para binário é {}'.format(numero, bin(numero)[2:]))
    
elif op == 2:
    print('O número escolhido foi {} e a sua conversão para octal é {}'.format(numero, oct(numero)[2:]))
    
elif op == 3:
    print('O número escolhido foi {} e a sua conversão para hexadecimal é {}'.format(numero, hex(numero)[2:]))
    
else:
    print('Escolha uma opção valida!!')