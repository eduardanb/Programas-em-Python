def prucurar_valor(matriz,x):
    for i in range(len(matriz)):
        for j in range(len(i)):
            if matriz[i][j] == valor:
                return i,j
    return None


matriz = []
x = int(input('Digite um valor para procurar: '))

for i in range(5):
    lista = []
    for j in range(5):
        valor = int(input('Informe o valor da posição ({} e {}): '.format(i,j)))
        lista.append(valor)
    matriz.append(lista)
localizacao = prucurar_valor(matriz,valor)

if localizacao:
    linha = coluna = localizacao
    print(f"O valor {valor} foi encontrado na posição ({linha}, {coluna}).")
else:
    print("O valor não foi encontrado na matriz.")