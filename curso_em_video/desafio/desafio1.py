# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
num = int(input('Digite um número inteiro: '))
a = num - 1
s = num + 1
print('o número digitado foi o {}, ele possui o antecessor {} e o sucessor {}.'.format(num, a, s))