# Lendo o vetor de 10 posições
vetor = []
for i in range(10):
    valor = int(input("Digite o valor da posição {}: ".format(i+1)))
    vetor.append(valor)

# Verificando valores repetidos
valores_repetidos = []
for elemento in vetor:
    if vetor.count(elemento) > 1:
        valores_repetidos.append(elemento)
print('Valores repetidos encontrados:',valores_repetidos)
