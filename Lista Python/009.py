lista = []
lista_par = []
lista_impar = []

num_inicial = int(input('Digite quantos elementos vai na lista: '))
for i in range(num_inicial):
    valores = int(input('Digite o {}º valor: '.format(i+1)))
    lista.append(valores)
    if valores % 2 == 0:
        lista_par.append(valores)
    else:
        lista_impar.append(valores)

print('Lista completa:',lista)
print('Lista com números pares:',lista_par)
print('Lista com números ímpares:',lista_impar)
