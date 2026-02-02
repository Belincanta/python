# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
import math
an = float(input('Digite um ângulo: '))
se = math.sin(math.radians(an))
co = math.cos(math.radians(an))
ta = math.tan(math.radians(an))
print(f'O ângulo {an} graus.')
print(f'Tem seu seno de {se:.2f}.')
print(f'Tem seu coseno de {co:.2f}.')
print(f'Tem sua tangente de {ta:.2f}.')