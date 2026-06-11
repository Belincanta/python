# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(j = "<desconhecido>", g = 0):
   print(f"O jogador {j} marcou {g} gol(s) no campeonato.")


#programa principal
jogador = input("Nome do jogador: ")
gol = input("Quantos gols ele marcou: ")
if gol.isnumeric(): #se estiver preenchido e for um número, vai mandar para a função este número
    gol = int(gol)
else:
    gol = 0 #se não mando para a função 0 gols

if jogador.strip() == "": #se tirando os espaços não sobrar nada, ou seja está vazio, vai mandar só a qtde de gols
    ficha(g = gol)
else:
    ficha(jogador, gol) #se não mando para a função ambas parâmetros
   