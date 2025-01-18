num = int(input("Digite um valor inteiro: "))

print("Digite [1] para converter em binário")
print("Digite [2] para converter em octal")
print("Digite [3] para converter em hexadecimal")

opcao = int(input("Opção: "))

if opcao == 1:
    print("O número {} em binário é {}".format(num, bin(num)[2:])) #[2:] tira a verificação do binário

elif opcao == 2:
    print("O número {} em octal é {}".format(num, oct(num)[2:])) #[2:] tira a verificação do octal

elif opcao == 3:
    print("O número {} em octal é {}".format(num, hex(num)[2:])) #[2:] tira a verificação do hexadecimal

else:
    print("Opção inválida")