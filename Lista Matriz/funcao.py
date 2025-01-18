def criar_matriz(linha,coluna):
    matriz = []
    for i in range(linha):
        matriz.append([0]*coluna)
    return matriz
def ler_matriz(matriz,linha,coluna):
    for i in range(linha):
        for j in range(coluna):
            matriz[i][j] = int(input(f'M[{i},{j}]: '))
    return matriz
def diagonal_inversa(matriz,ordem):
    for i in range(ordem):
        for j in range(ordem):
            if i + j == ordem-1:
                matriz[i][j] = 1
    return matriz
def identidade(matriz,ordem):
    for i in range(ordem):
        matriz[i][i] = 1
    return matriz
def transposta(matriz,linha,coluna):
    transposta = criar_matriz(coluna,linha)
    for i in range(linha):
        for j in range(coluna):
            transposta[j][i] = matriz[i][j] 
    return transposta
def imprimir_matriz(matriz,linha,coluna):
    for i in range(linha):
        for j in range(coluna):
            print(f'[{matriz[i][j]:^5}]',end = '')
print()