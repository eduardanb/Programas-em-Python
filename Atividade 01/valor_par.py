contador = 0 #Faz a contagem dos valores fornecidos.

for i in range(1,6): #Laço de repetição que ocorre de 1 até 5.
    valores = int(input('Informe valores inteiros: ')) #Entrada de valores
    if valores % 2 == 0: #Condição par
        contador = contador + 1 #Incrementação de valores

print('{} valores pares'.format(contador)) #Apresentação
