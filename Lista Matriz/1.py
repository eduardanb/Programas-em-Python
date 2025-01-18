matriz = []
contador = 0
for i in range(4):
    linha = []
    for j in range(4):
        valor = int(input('Digite o valor da posição {} e {}: '.format(i,j)))
        linha.append(valor)
    matriz.append(linha)

for linha in matriz:
    for valor in linha:
        if valor > 10:
            contador = contador + 1
print(contador,'Valores encontrados.')
