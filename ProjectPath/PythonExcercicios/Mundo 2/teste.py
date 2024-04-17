#Escreva um programa que solicite o percentual de crescimento de produção de uma empresa 
#e informe se houve um crescimento (porcentagem positiva) ou decrescimento (porcentagem negativa).



crsc = float(input('Digite o percentual de crescimento da empresa: '))

if crsc == 0:
    print(f'Conforme os valores informados, não houve crescimento. {crsc}%')
elif crsc > 0:
    print(f'Parabéns, sua empresa teve um crescimento de {crsc}%')
else:
    print(f'Sua empresa teve um decrescimento de {crsc}%')