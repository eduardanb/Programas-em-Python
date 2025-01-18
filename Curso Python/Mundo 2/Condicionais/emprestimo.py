valor = float(input("Digite o valor da casa: R$"))
salario = float(input("Digite o seu salário: R$"))
anos = float(input("Digite em quantos anos você vai pagar: "))
prestacao = valor / (anos * 12)

if prestacao <= salario * 30 / 100:
    print("O empréstimo no valor de {:.2f}R$ foi deferido!".format(prestacao))

else:
    print("Empréstimo negado!")
