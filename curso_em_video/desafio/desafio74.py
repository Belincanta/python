# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
while True:
    numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
    print("="*40)
    print(f"Os números sorteados foram {numeros}")
    print(f"O número maior é o {max(numeros)}") # função nativa das tuplas
    print(f"O número menor é o {min(numeros)}") # função nativa das tuplas
    print("="*40)
    opcao = " "
    while opcao not in "SN":
        opcao = input("Quer gerar novos números? S/N: ").strip().upper()[0]
    if opcao == "N":
        break
print("Fim do programa")

