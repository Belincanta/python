#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
ano_atual = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    ano_nascimento = int(input(f"Digite em que ano a {c}º pessoa nasceu: "))
    if (ano_atual - ano_nascimento) >= 18:
        maior += 1
    else:
        menor += 1
print(f"Tivemos {maior} pessoas com maioridade.\nTivemos ainda {menor} pessoas com menoridade")
