# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

analise = dict()
total_gols = list()
analise["jogador"] = input("Nome do jogador: ")
partidas = int(input(f"Quantas partidas {analise['jogador']} jogou: "))
for g in range(partidas):
    total_gols.append(int(input(f"Quantos gols {analise['jogador']} fez no jogo {g+1}: ")))
analise["gols"] = total_gols[:] #para colocar a lista dentro do dicionário, criando uma cópia
analise["total"] = sum(total_gols) # somar o total de gols
print("=-"*15)
print(analise)
print("=-"*15)
for k, v in analise.items(): # repetição para varrer o dicionário
    print(f"No campo {k} tem {v}")
print("=-"*15)
print(f"O jogador {analise['jogador']} fez {len(analise['gols'])} partidas.")
for i, v in enumerate(analise["gols"]):
    print(f"Na partida {i} foram marcados {v} gols.")