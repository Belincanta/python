# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date #importar a biblioteca de data
ano_atual = date.today().year
ano = int(input("Em que ano você nasceu? "))
sexo = input("Você é homem? (s ou n): ")
idade = ano_atual - ano
if idade == 18 and sexo == "s":
    print(f"Você tem que se alistar IMEDIATAMENTE, pois possui {idade} anos.")
elif idade < 18 and sexo == "s":
    saldo = 18 - idade
    print(f"Você ainda não possui a idade necessária para se alistar.\nAinda faltam {saldo} anos para o alistamento.\nVocê irá se alistar em {(18 - idade) + date.today().year}!")
elif idade > 18 and sexo == "s":
    saldo = date.today().year - (idade - 18)
    ano_alistamento = date.today().year - saldo
    print(f"Você não possui mais idade para se alistar.\nVocê deveria ter se alistado há {ano_alistamento} anos anos atrás.\nVocê se alistou em {saldo}!")
else:
    print("Você não tem obrigatóriedade para se alistar")