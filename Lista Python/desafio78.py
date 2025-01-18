lista = []
for i in range(1,6):
    lista.append(int(input('Digite um valor: ')))
lista.sort()
print('Lista =',lista)
print('Maior termo inserido:', max(lista))
print('Menor termo inserido:', min(lista))