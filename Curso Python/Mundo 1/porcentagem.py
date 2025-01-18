valor = float(input("Informe o valor do produto: "))
desconto = valor - (valor * 5 / 100)

print("O valor do produto é {:.2f}R$,".format(valor), end=" ")
print("o seu novo preço na promoção é de {:.2f}R$.".format(desconto))

