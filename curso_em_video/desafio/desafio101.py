# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(a):
    from datetime import datetime #importando dentro da função, economiza memória.  
    idade = datetime.today().year - ano
    if idade < 16:
        print(f"Você tem {idade} anos, não vota!")
    elif idade >= 18 and idade < 65:
        print(f"Você tem {idade} anos, voto é obrigatório!")
    else:
        print(f"Você tem {idade} anos, voto é opcional!")

# programa principal
ano = int(input("Em que ano você nasceu? "))
voto(ano)