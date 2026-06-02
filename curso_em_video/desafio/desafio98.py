# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2 
# c) uma contagem personalizada

from random import random
from time import sleep

def contador(i, f, p):
    if p < 0: # pegar os passos negativos
        p *= -1
    if p == 0: # pegar os passos 0
        p = 1

    print("=-"*19)
    print(f"Contagem de {i} a {f} de {p}: ")
    sleep(2.5)    

    if i < f:
        c = i
        while c <= f:         
            print(f"{c}, ", end="", flush=True) 
            sleep(0.5)
            c+=p
        print("FIM!")
    else:
        c = i
        while c >= f:
            print(f"{c}, ", end="", flush=True)
            sleep(0.5)
            c-=p
        print("FIM!")

contador(1, 10, 1)
contador(10, 0, 2)
print("=-"*19)
print("Agora você vai determinar a contagem: ")
inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
contador(inicio, fim, passo)