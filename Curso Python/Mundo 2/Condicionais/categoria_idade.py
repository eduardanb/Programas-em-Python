print("Programa categoria de idades")

print()

ano_nascimento = int(input("Digite seu ano de nascimento: "))
ano_atual = int(input("Informe o ano que deseja calcular: "))
idade = ano_atual - ano_nascimento

print()
print("O(A) atleta tem {} anos.".format(idade))
print()

if idade <= 0:
    print()
    print("Idade inválida, não possui categoria")
    print()

elif idade > 0 and idade <= 9:
    print()
    print("Categoria: MIRIM")
    print()

elif idade >= 10 and idade <= 14:
    print()
    print("Categoria: INFANTIL")
    print()

elif idade >= 15 and idade <=19:
    print()
    print("Categoria: JUNIOR")
    print()

elif idade == 20:
    print()
    print("Categoria: SÊNIOR")
    print()

else:
    print()
    print("Categoria: MASTER")
    print()