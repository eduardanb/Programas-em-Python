a = 80000
b = 200000
taxa_a = 0.03
taxa_b = 0.015
anos = 0
while a < b:
    a = a + int(taxa_a * a)
    b = b + int(taxa_b * b)
    anos = anos + 1
print("{} anos: ".format(anos))
