#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input(f"Digite o peso da {c}ª pessoa: "))
    if c == 1:
        maior = peso #estou dizendo que o primeiro valor é o maior
        menor = peso #estou dizendo que o primeiro valor é o menor
    else:
        if peso > maior: #se o próximo número for maior que o segundo, ele será o maior.
            maior = peso
        if peso < menor: #se o próximo número for menor que o segundo, ele será o menor.
            menor = peso
print(f"O maior peso entre as pessoas é o {maior}kg.")
print(f"O menor peso entre as pessoas é o {menor}kg.")