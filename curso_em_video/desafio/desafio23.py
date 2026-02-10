# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
numero = int(input('Digite aqui um número: '))
print(f'Unidade: {numero // 1 % 10}')
print(f'Dezena: {numero // 10 % 10}')
print(f'Centena: {numero // 100 % 10}')
print(f'Milhar {numero // 1000 % 10}')

# // é uma divisão
# % 10 quer dizer que está dividindo o resto da divisão por 10