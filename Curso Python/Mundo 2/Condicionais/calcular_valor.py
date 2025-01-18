pagar = float(input("Digite o valor do produto: "))
condicao = input("Informe a condição do pagamento: ")

if condicao == "dinheiro" or condicao == "cheque":
    desconto = pagar - (pagar * 10 / 100)
    print("O valor do produto é de {} R$, mas com '10%' de desconto para dinheiro/cheque fica por {}R$.".format(pagar,desconto))

elif condicao == "cartão":
    desconto = pagar - (pagar * 5 / 100)
    print("O valor do produto é de {} R$, mas com o '5%' de desconto para cartão fica por {}R$.".format(pagar))

elif condicao =="2x no cartão":
    print("O preço a ser pago é de {} R$, não possui desconto!.")

elif condicao =="3x no cartão":
    juros = pagar + (pagar * 20 / 100) 
    print("O valor do produto é de {} R$, mas parcelado 3x ou mais no cartão fica por {}R$.".format(pagar,juros))

else:
    print("Condição inválida!")

    print("")