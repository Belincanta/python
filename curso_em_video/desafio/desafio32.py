# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date #importar da biblioteca a data
ano = int(input("Em que ano quer analisar, se ele é bissexto? Digite 0 para saber sobre o ano atual: "))
if ano == 0:
    ano = date.today().year # pega o ano da data de hoje
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print(f"o ano {ano} é bissexto")
else:
    print(f"O ano {ano} não é bissexto")

# % 4 == 0 - ou seja, pode ser divisível por 4, sobrando 0
# % 100 != - ou seja, não pode ser divisível por 100 completo por completo
# % 400 ==0 - ou seja, pode ser divisivel por 400, sobrando 0