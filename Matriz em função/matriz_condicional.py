def gerar_matriz():
    matriz = []
    for i in range(10):
        linha = []
        for j in range(10):
            if i < j:
                elemento = 2*i + 7*j - 2
            elif i == j:
                elemento = 3*i**2 - 1
            else:
                elemento = 4*i**3 - 5*j**2 + 1
            linha.append(elemento)
        matriz.append(linha)
    return matriz

def imprimir_matriz(matriz):
    for linha in matriz:
        for elemento in linha:
            print(elemento, end='\t')
        print()

matriz = gerar_matriz()
imprimir_matriz(matriz)