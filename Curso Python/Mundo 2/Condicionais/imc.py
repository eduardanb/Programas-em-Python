print("Calcule seu Índice de Massa Corpórea, IMC")
print()

peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua altura: "))
imc = peso / (altura**2)

print()
print("De acordo com seu peso {}kg e sua altura {}m, seu IMC é {:.2F}.".format(peso,altura,imc))

if imc < 18.5:
    print("Situação: ABAIXO DO PESO")

elif imc >= 18.5 and imc <= 25:
    print()
    print("Situação: PESO IDEAL")

elif imc > 25 and imc <=30:
    print()
    print("Situação: SOBREPESO")

elif imc > 30 and imc <=40:
    print()
    print("Situação: OBESIDADE")

else:
    print()
    print("Situação: OBESIDADE MÓRBIDA")