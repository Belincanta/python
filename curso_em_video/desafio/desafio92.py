#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime

trabalhador = {}
trabalhador["Nome"] = input("Nome: ")
nascimento = int(input("Ano de nascimento: "))
trabalhador["Idade"] = datetime.now().year - nascimento
trabalhador["CTPS"] = int(input("Possui CTPS (0 não possui): "))
if trabalhador["CTPS"] != 0:
    trabalhador["Ano contratação"] = int(input("Ano de contratação: "))
    trabalhador["Salário"] = float(input("Salário R$ "))
    trabalhador["Aposentadoria"] = trabalhador["Idade"] + ((trabalhador["Ano contratação"] + 35) - datetime.now().year)
print("=-"*20)
for k, v in trabalhador.items():
    print(f" - {k} tem o valor {v}!")