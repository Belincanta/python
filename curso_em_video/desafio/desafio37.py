#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
numero = int(input("Digite um número: "))
print("Escolha uma das opções abaixo: ")
print("[1] para binário.\n[2] para octal.\n[3] para hexadecimal.")
opcao = int(input("Digite a sua opção: "))
if opcao == 1:
    print(f"O número {opcao} convertido para binário é {bin(numero) [2:]}.") 
elif opcao == 2:
    print(f"O número {opcao} convertido para octal é {oct(numero) [2:]}.")
elif opcao == 3:
    print(f"O número {opcao} convertido para hexadecimal é {hex(numero) [2:]}.")
else:
    print("Você escolheu uma opção inválida, favor verificar.")

    #[2:] é um fatiamento, pois quando transporma o número, o inicio é 0b, 0o ou 0x