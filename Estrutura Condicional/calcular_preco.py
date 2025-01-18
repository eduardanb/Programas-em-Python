#Faça um programa que pergunte o preço de três produtos e informe 
#qual produto você deve comprar, sabendo que a decisão é sempre
#pelo mais barato.

valor1 = float(input("Informe o valor do primeiro produto: "))
valor2 = float(input("Informe o valor do segundo produto: "))
valor3 = float(input("Informe o valor do terceiro produto: "))

if valor1 < valor2 and valor1 < valor3:
    print("O produto indicado para a compra é o que custa",valor1)

elif valor2 < valor1 and valor2 < valor3:
    print("O produto indicado para a compra é o que custa",valor2)

else:
    print("O produto indicado para a compra é o que custa",valor3)