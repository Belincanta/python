#Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0 #acumulador
cont = 0 #acumulador
for n in range(1, 501, 2):
    if n % 3 == 0:
        soma += n #vai somar todos os números
        cont += 1 #vai contar quantos números tem
print(f"A soma dos {cont} valores é de {soma}")
