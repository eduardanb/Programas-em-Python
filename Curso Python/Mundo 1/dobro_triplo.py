num = int(input('Digite um valor: '))
dobro = num + num
triplo = dobro + num
raizq = num ** (1/2)

print("o dobro de {} vale {}".format(num,dobro))
print("o triplo de {} vale {}".format(num,triplo))
print("a raíz quadrada de {} vale {:.3f}".format(num,raizq))