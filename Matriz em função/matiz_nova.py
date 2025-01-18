def matriz_com_maiores_valores(matriz1,matriz2):
    matriz3 = []
    for i in range(2):
        linha = []
        for j in range(2):
            valor = max(matriz1[i][j], matriz2[i][j])
            linha.append(valor)
        matriz3.append(linha)
    return matriz3

matriz1 = []
matriz2 = []

for i in range(2):
    linha = []
    for j in range(2):
        valor = int(input('Informe o valor da posição ({} e {}): '.format(i,j)))
        linha.append(valor)
    matriz1.append(linha)

for i in range(2):
    linha = []
    for j in range(21):
        valor = int(input('Informe o valor da posição ({} e {}): '.format(i,j)))
        linha.append(valor)
    matriz2.append(linha)

matriz_maior_valor = matriz_com_maiores_valores(matriz1,matriz2)
for i in range(len(matriz_maior_valor)):
    print(matriz_maior_valor[i])