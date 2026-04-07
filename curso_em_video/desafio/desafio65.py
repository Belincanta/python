# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores
contador = soma = media = maior = menor = 0
seguir = "S"
while seguir == "S":
    numero = int(input("Digite um número: "))
    seguir = input("Deseja seguir [S / N]: ").upper()
    contador += 1
    soma += numero
    if contador == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
media = soma / contador #para não precisar calcular a média em toda repetição   
print(f"""
Você digitou {contador} números, obetendo uma média de {media:.2f}!
O maior número é {maior} e o menor número é o {menor}""")
