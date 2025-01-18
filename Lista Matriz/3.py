# Criar as matrizes vazias
matriz1 = []
matriz2 = []

# Solicitar ao usuário para inserir os valores da primeira matriz
print("Insira os valores da primeira matriz:")
for i in range(2):
    linha = []
    for j in range(2):
        valor = int(input(f"Insira o valor da posição ({i+1}, {j+1}): "))
        linha.append(valor)
    matriz1.append(linha)

# Solicitar ao usuário para inserir os valores da segunda matriz
print("Insira os valores da segunda matriz:")
for i in range(2):
    linha = []
    for j in range(2):
        valor = int(input(f"Insira o valor da posição ({i+1}, {j+1}): "))
        linha.append(valor)
    matriz2.append(linha)

# Criar a terceira matriz com os maiores valores
matriz3 = []
for i in range(2):
    linha = []
    for j in range(2):
        maior_valor = max(matriz1[i][j], matriz2[i][j])
        linha.append(maior_valor)
    matriz3.append(linha)

# Imprimir a terceira matriz
print("A terceira matriz com os maiores valores é:")
for linha in matriz3:
    print(linha)