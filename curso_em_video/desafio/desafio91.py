#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter #para organizar em ordem crescente um valor no dicionário.
dados = {"jogador1": randint(1,6),
         "jogador2": randint(1,6),
         "jogador3": randint(1,6),
         "jogador4": randint(1,6)
}
ranking = list()
print("=-"*15)
print("Valores sorteados:")
for k, v in dados.items(): #for do dicionário
    print(f"{k} jogou {v} no dado.")
    sleep(1)

# dados do ranking
print("=-"*15)
print("Ranking final:")
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True) #para pegar o valor do dado
for i, v in enumerate(ranking): # for da lista
    print(f"{i+1}º lugar: {v[0]} com {v[1]}")
    sleep(1)
