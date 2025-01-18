for a in range(0,11): # Para i no intervalo de 0 a 10 (o último valor não conta)
    print(a) # Repete o valor no intervalo determinado
print("Fim")

print()

#-------------------------------------------------------------------------------

for i in range(10,0,-1): # Decresce
    print(i)
print("Fim")

print()

#-------------------------------------------------------------------------------

inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

for b in range(inicio, fim + 1, passo):
    print(b)