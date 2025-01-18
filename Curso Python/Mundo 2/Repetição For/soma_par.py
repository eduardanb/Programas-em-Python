soma = 0
for i in range(1,7):
    valores = int(input("Informe o {}º valor: ".format(i)))
    if valores % 2 == 0:
        soma = soma + valores
print("A soma dos valores pares é igual a {}".format(soma))