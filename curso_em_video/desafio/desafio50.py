#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input(f"Digite o {c}º número: "))
    if num % 2 == 0:
        soma += num #vai retornar a soma dos números pares
        cont += 1 #mostra a quantidade de números pares
print(f"A soma dos {cont} números pares informados é {soma}")