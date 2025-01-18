A = float(input(''))
B = float(input(''))
C = float(input(''))

if A >= B + C:
    print("NAO FORMA TRIANGULO")
else:
    if A ** 2 == B ** 2 + C ** 2:
        print("TRIANGULO RETANGULO")
    elif A ** 2 > B ** 2 + C ** 2:
        print("TRIANGULO OBTUSANGULO")
    else:
        print("TRIANGULO ACUTANGULO")
    if A == B == C:
        print("TRIANGULO EQUILATERO")
    elif A == B or A == C or B == C:
        print("TRIANGULO ISOSCELES")




if A >= B + C:
    print("NAO FORMA TRIANGULO")
else:
    if A ** 2 == B ** 2 + C ** 2:
        print("TRIANGULO RETANGULO")
    if A ** 2 > B ** 2 + C ** 2:
        print("TRIANGULO OBTUSANGULO")
    if A ** 2 < B ** 2 + C ** 2:
        print("TRIANGULO ACUTANGULO")
    if A == B == C:
        print("TRIANGULO EQUILATERO")
    elif A == B or A == C or B == C:
        print("TRIANGULO ISOSCELES")