# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
numero = int(input('Digite um número qualquer: '))
resultado = numero % 2 #pega o resto da divisão do número digitado e divide por 2, se for 0 é par, 1 é impar.
if resultado == 0:
    print(f'O número {numero} é PAR')
else:
    print(f'O número {numero} é IMPAR')
