valor_abastecer = float(input("Digite o valor do litro de combustível: "))
valor_dinheiro = float(input("Digite quanto em dinheiro você deseja abastecer: "))
litro = valor_abastecer / valor_dinheiro

print("Você irá obter {:.2f} litros de combustível.".format(litro))