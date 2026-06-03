# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep

def maior(*num):
    cont = maior = 0
    print("="*30)
    print("Analisando os números...")
    for valor in num:
        print(f"{valor} ", end="", flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f"\nForam encontrados {cont} números.")
    print(f"O maior número entre eles é o {maior}.")


#programa principal
maior(7, 9, 8, 5, 6, 1)
maior(2, 0, 5, 7, 8)
maior(2, 5, 4)