# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

analise = dict()
total_gols = list()
time = list()
while True:
    analise.clear()
    analise["jogador"] = input("Nome do jogador: ")
    partidas = int(input(f"Quantas partidas {analise['jogador']} jogou: "))    
    total_gols.clear()
    for g in range(partidas):
        total_gols.append(int(input(f"Quantos gols {analise['jogador']} fez no jogo {g+1}: ")))
    analise["gols"] = total_gols[:] #para colocar a lista dentro do dicionário, criando uma cópia
    analise["total"] = sum(total_gols) # somar o total de gols
    time.append(analise.copy())
    resp = input("Quer continuar? S/N: ").upper()[0]
    while True:
        if resp in "SN":
            break
        print("ERRO! Digite S ou N:")
    if resp == "N":
        break

# dados dos jogadores
print("-"*40)
for k, v in enumerate(time):
    print(f"{k:>4} | ", end="")
    for d in v.values():
        print(f"{str(d):<15}", end="")
    print()
print("-"*40)

# dados para análise individual
print("=-"*20)
while True:
    busca = int(input("Quer analisar qual jogador? [999 para sair]: "))
    if busca == 999:
        break
    if busca >= len(time):
        print("Erro! Este jogador não foi cadastrado.")
    else:
        print(f"--- Levantamento do jogador {time[busca]["jogador"]}:") 
    for i, v in enumerate(time[busca]["gols"]):
        print(f"Na partida {i+1} foram marcados {v} gols.")
print("=-"*20)
print("VOLTE SEMPRE")

