for c in range(7, 0, -1): #CONTAGEM REGRESSIVA 
    print(c)

#O for sempre vai ignorar o ultimo numero

for c in range (0, 7): #CONTAGEM CRESCENTE
    print(c)


for c in range (0, 7, 2): #Pulando de 2 em 2
    print(c)


n = int(input('Digite um numero interio: '))
for c in range (0, n+1):
    print(c)
print('Fim')

s = 0
for c in range (0 , 4): #SOMAR VARIOS NUMEROS
    n = int(input('Digite um numero: '))
    s += n
print('O somatório de todos os valores foi {}' .format(s))

