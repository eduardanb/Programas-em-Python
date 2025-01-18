num = int(input('Digite um número: '))
sucessor = num + 1
antecessor = num -1

print('O antecessor é {}'.format(antecessor), end='')
print(' {:-^3}'.format(num), end=" ")
print('e o sucessor é {}'.format(sucessor))