#Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

from time import sleep
numero = 0
for numero in range(2, 51, 2):
    sleep(0.5)
    print(numero)
print("Contagem finalizada")