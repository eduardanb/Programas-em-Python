N = int(input())
cont = 0
a = 1
b = 2
c = 3
while cont < N:
    
    print('{} {} {} PUM'.format(a,b,c))
    c = c + 2 
    a = c
    b = c
    b = b + 1
    c = c + 2
    cont = cont + 1         