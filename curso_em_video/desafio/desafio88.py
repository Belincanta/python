# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import sample
from time import sleep
jogos = []
palpite = []
print("*"*30)
print(f"{"MEGA SENA":^30}")
print("*"*30)
qtde_jogos = int(input("Quantos jogos vai querer sortear? "))
for j in range(qtde_jogos):
    palpite = sample(range(1, 61), 6)
    palpite.sort()    
    jogos.append(palpite[:])
    palpite.clear()
print(f"*"*5,f"Sorteando {qtde_jogos} jogos", "*"*5)
for i, l in enumerate(jogos):
    sleep(1)
    print(f"Jogo {i+1} sorteou os números {l}")
print(f"-"*15, "< Boa Sorte >", "-"*15)
