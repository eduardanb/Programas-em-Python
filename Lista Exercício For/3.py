soma = 0
for i in range(1, 11):
    num = int(input('Informe o {} número: '.format(i)))
    soma = soma + num
    media = soma / 10
print("A soma dos números é {} e a média é {:.2f}".format(soma,media))