a = [1, 0, 5, -2, -5, 7]
soma = a[0] + a[1] + a[5]
a.insert(4,100)
print(a)
print('A soma dos números', a[0],',', a[1],',', a[5], 'é', soma, sep=' ')
for i in range(len(a)):
    print(a[i])