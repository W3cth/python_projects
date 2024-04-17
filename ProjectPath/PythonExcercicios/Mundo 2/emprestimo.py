vc = float(input('Qual valor da casa ? '))
salario = float(input('Qual seu salário ? '))
anos = int(input('Quantos anos de financiamento ? '))
minimo = salario * 30 / 100
prestação = vc / (anos * 12)
print('O valor da casa é R${:.2f}, o seu salário é R${:.2f} e a prestação será R${:.2f} '.format(vc, salario, prestação))

if prestação <= minimo:
    print('Seu salario é compativel com o valor das prestações')
    
else:
    print('Seu salario não é compativel com o valor das prestações')