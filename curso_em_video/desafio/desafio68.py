# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
vitorias = 0
while True:
    jogador = int(input("Digite um número: "))
    computador = randint(0, 10)
    resultado = (jogador + computador) % 2
    opcao = " "    
    while opcao not in "PI":
        opcao = input("Par ou Impar (P/I): ").strip().upper()[0]    
    if resultado == 0: #PAR
        if opcao == "P":
            print(f"Você VENCEU!")
            vitorias += 1
        else:
            print(f"Você PERDEU!")
            break
    if resultado != 0: #IMPAR
        if opcao == "I":
            print(f"Você VENCEU!")
            vitorias += 1
        else:
            print(f"Você PERDEU!")
            break
    print(f"Escolheu {jogador} e o computador {computador}, dando {jogador + computador} - ", end = "")
    print("DEU PAR" if resultado == 0 else "DEU ÍMPAR")
print(f"GAME OVER, você escolheu {jogador} e o computador {computador}, dando {jogador + computador}, você conseguiu {vitorias} vitórias seguidas.")
