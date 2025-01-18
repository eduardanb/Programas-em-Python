num = int(input("Informe um valor inteiro menor que 1000: "))
centenas = num // 100
resto = num % 100
dezenas = resto // 10
unidades = resto % 10

if num < 1000 and num > 0:
    if centenas > 1 and dezenas > 1 and unidades > 1:
        print(centenas,"centenas,", dezenas,"dezenas e",unidades,'unidades.')

else:
    print("Preste atenção!, o número deve ser menor do que 1000! ")