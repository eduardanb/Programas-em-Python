print("Calcule o preço a pagar pelo aluguel do seu carro")

print()

quant_km = float(input("Informe a quantidade de Km percorridos: "))
quant_dias = float(input("Informe a quantidade de dias que ele foi alugado: "))
pagar = (quant_dias * 60) + (quant_km * 0.15)

print()

print("O total a pagar é de {:.2f}R$.".format(pagar))