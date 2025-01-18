totmaior = 0
totmenor = 0
ano_atual = int(input("Ano atual: "))
for i in range(1, 8):
    nascimento = int(input('Data nascimento: '))
    idade = ano_atual - nascimento
    if idade >= 18:
        totmaior = totmaior + 1
    else:
        totmenor = totmenor + 1

print("{} pessoas maiores de idade.".format(totmaior))
print("{} pessoas menores de idade.".format(totmenor))

