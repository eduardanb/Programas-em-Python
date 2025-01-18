print()

ano_nascimento = int(input("Informe o seu ano de nascimento: "))
ano_atual = int(input("Informe o ano atual: "))
idade = ano_atual - ano_nascimento

print()

print("Você nasceu no ano de {} e têm {} anos.".format(ano_nascimento,idade))

print()

if ano_nascimento < 0:
    print("Idade inválida!")

elif ano_nascimento > 0 and ano_nascimento <= 18:
    saldo = 18 - idade
    print("Faltam {} anos para o alistamento.".format(saldo))

elif ano_nascimento == 18:
    print('Você tem que se alistar imediatamente.')

else:
    saldo = idade - 18
    print("Você devera ter se alistado há {} anos.".format(saldo))

    print()
    