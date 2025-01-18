print()

print("Calcule sua média!")

print()

nota1 = float(input("Informe sua primeira nota: "))
nota2 = float(input("Informe sua segunda nota: "))
media = (nota1 + nota2) / 2

print()

print("Calculando as notas {} e {}, a média do aluno é {}".format(nota1,nota2,media))

print()

if media < 5.0:
    print()
    print("Situação: Reprovado(a)")

elif media >= 5.00 and media <= 6.9:
    print()
    print("Situação: Recuperação")

else:
    print()
    print("Situação: Aprovado(a)")
    print()