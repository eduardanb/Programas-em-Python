#Formatação de resultados decimais
valor1 = int(input("Digite um valor: "))
valor2 = int(input("Digite outro valor: "))
div = valor1 / valor2
print("A divisão entre {} e {} é {:.2f}".format(valor1,valor2,div))
