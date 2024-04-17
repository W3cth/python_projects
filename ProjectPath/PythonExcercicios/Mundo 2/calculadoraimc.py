peso = float(input('Digite seu peso em KGs: '))
altura = float(input('Digite sua altura em Metros: '))
idade = int(input('Digite sua idade: '))
imc = peso / (altura**2)


if imc <= 18.5:
    print('O seu IMC é de {:.2f} e você está com Magreza! Procure comer mais!'.format(imc))
          
elif imc >= 18.5 and imc <= 24.9:
    print('O seu IMC é de {:.2f} e você está Normal! Parabens!'.format(imc))

elif imc >= 25 and imc <= 29.9:
    print('O seu IMC é de {:.2f} e você está com Sobrepeso! Reduza o rango!'.format(imc))

elif imc >= 30 and imc <= 39.9:
    print('O seu IMC é de {:.2f} e você está com Obesidade! Hora de parar, antes que seja tarde!'.format(imc))

elif imc > 40:
    print('O seu IMC é de {:.2f} e você está com Obesidade GRAVE! Procure um médico imediatamente!'.format(imc))

