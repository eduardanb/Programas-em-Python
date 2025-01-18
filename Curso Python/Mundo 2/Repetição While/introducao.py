c = 1 

while c < 10:
    print(c)
    c = c + 1
print('fim')

print()
print('--------------------------------')
print()

n = 1
while n != 0:
    n = int(input('Informe um valor: '))
print('Fim')

print()
print('--------------------------------')
print()

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        par = par + 1
    else: 
        impar = impar + 1
print('Você digitou {} numeros pares e {} números ímpares.'.format(par,impar))
