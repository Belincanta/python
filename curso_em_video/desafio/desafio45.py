#Crie um programa que faça o computador jogar Jokenpô com você.
items = ("Pedra", "Papel", "Tesoura")
from random import randint
from time import sleep

#opção aleatório que o computador irá selecionar
computador = randint(0, 2)

#opção para o jogador escolher
print("""=== Suas opções ===:
      [0] PEDRA
      [1] PAPEL
      [2] TESOURA""")
jogador = int(input("Escolha uma das opções acima: "))
print("=" * 22)

#tempo para retornar o resultado
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PÔ!!")

#retorno do que cada um escolheu
print(f"Computador escolheu {items[computador]}")
print(f"Você escolheu {items[jogador]}")
print("="* 22)

#condições aninhadas
if computador == 0: #computador jogou pedra
    if jogador == 0: #jogador jogou pedra
        print("EMPATOU")
    elif jogador == 1: #jogador jogou papel
        print("Você GANHOU do computador")
    elif jogador == 2: #jogador jogou tesoura
        print("Você PERDEU do computador")
    else:
        print("Jogada INVÁLIDA, tente novamente")

elif computador == 1: #computador jogou papel
    if jogador == 0: #jogador jogou pedra
        print("Você PERDEU do computador")
    elif jogador == 1: #jogador jogou papel
        print("EMPATOU")
    elif jogador == 2: #jogador jogou tesoura
        print("Voce GANHOU do computador")
    else:
        print("Jogada INVÁLIDA, tente novamente")

elif computador == 2: #computador jogou tesoura
    if jogador == 0: #jogador jogou pedra
        print("Você GANHOU do computador")
    elif jogador == 1: #jogador jogou papel
        print("você PERDEU do computador")
    elif jogador == 2: #jogador jogou tesoura
        print("EMPATOU")
    else:
        print("Jogada INVÁLIDA, tente novamente")
