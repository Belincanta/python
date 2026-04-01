# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.


# 1 tentativa:

# from random import randint #importa a lib de números aleatórios
# tentativa = 1
# proximidade = 0
# computador = randint(0, 10) #gera um número aleatório de 0 a 10
# jogador = int(input("Estou pensando em um número de 0 a 10, tente adivinhar!\nQual é o seu palpite? "))
# while computador != jogador: #enquanto os números forem diferentes
#     if computador > jogador:
#         proximidade = "MAIS"
#     elif computador < jogador:
#         proximidade = "MENOS"
#     jogador = int(input(f"Você errou! É {proximidade}. Tente novamente: "))
#     tentativa +=1
# print(f"Você acertou! Foi preciso {tentativa} tentativas.")


# outra forma mais elegante:
from random import randint #importa a lib de números aleatórios
computador = randint(0, 10)
print("Estou pensando em um número de 0 a 10, tente adivinhar!")
acertou = False
tentativa = 0
while not acertou:
    jogador = int(input("Qual é o seu palpite? "))
    tentativa += 1
    if computador == jogador:
        acertou = True
    else:
        if computador > jogador:
            print("É mais... tente novamente!")
        elif computador < jogador:
            print("É menos... tente novamente!")
print(f"Você ACERTOU! Foram necessárias {tentativa} tentativas.")




