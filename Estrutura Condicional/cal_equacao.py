#Faça um programa que leia os coeficientes de uma equação do segundo grau.
#Inicialmente, verifique se se trata de uma equação do segundo grau e,
#caso positivo, calcule as reízes da equação.

import math #essa função calcula a raíz quadrada
a = float(input("Digite o primeiro coeficiente: "))
b = float(input("Digite o segundo coeficiente: "))
c = float(input("Digite o terceiro coeficiente: "))

if a == 0: 
    print("Não é equação do 2º grau!")
else:
    delta = b**2 - 4 * a * c
    print("O delta é:",delta)
    if delta > 0:
        #r1 = -b + delta**(1/2)
        r1 = (-b + math.sqrt(delta)) / (2*a)
        r2 = (-b - math.sqrt(delta)) / (2*a)
        print("Duas raízes reais:",r1,"e",r2)
    elif delta == 0:
        raiz = -b / (2*a)
        print("Uma raíz real:", raiz)
    else: 
        print("Não há raizes reais")