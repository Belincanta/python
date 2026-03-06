#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#– Até 9 anos: MIRIM
#– Até 14 anos: INFANTIL
#– Até 19 anos: JÚNIOR
#– Até 25 anos: SÊNIOR
#– Acima de 25 anos: MASTER

from datetime import date #importar a biblioteca de data
ano = int(input("Em que ano o atleta nasceu? "))
idade = date.today().year - ano
print(f"O atleta tem {idade} anos!")
if idade <= 9:
    print("Categoria: MIRIM")
elif idade >= 10 and idade <= 14:
    print("Categoria: INFANTIL")
elif idade >= 15 and idade <= 19:
    print("Categoria: JÚNIOR")
elif idade >= 20 and idade <= 25:
    print("Categoria: SÊNIOR")
else:
    print("Categoria: MASTER")