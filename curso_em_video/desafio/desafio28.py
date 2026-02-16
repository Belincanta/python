#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint #módulo para retornar um número inteiro aleatório
from time import sleep #módulo para criar uma espera na resposta
computador = randint(0,5) #vai sortear um número de 0 a 5
print('=-='*18) #cria uma barra 
print('Vou pensar em um número de 0 a 5. Tenta adivinhar...')
print('=-='*18) #cria uma barra  
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print(f'Você acertou, eu pensei no número {computador} mesmo, parabéns!')
else:
    print(f'Você errou, eu havia pensado no número {computador}, tente novamente!')