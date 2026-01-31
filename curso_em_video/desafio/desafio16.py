# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

import math
num = float(input('Digite um número: '))
print(f'O valor digitado {num} e sua porção inteira é {math.trunc(num)}')

#trunc é uma função dentro da biblioteca math que corta a parte inteira do número.