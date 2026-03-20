#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = int(input("Digite um número: "))
total = 0
for c in range(1, numero + 1):    
    if numero % c == 0: #se o número é divisível pelo contador e restar 0 é primo.
        print("\033[33m", end="") #código de cor
        total += 1 #total vez que for primo vai somar +1 no total
    else:
        print("\033[31m", end="") #código de cor
    print(c , end=" ")
print(f"\33[m\nO número {numero} foi dividido por {total} números.")
if total == 2:
    print(f"Portanto o número {numero} é primo, porque é divisível por 1 e por ele mesmo.")
else:
    print(f"Portando o número {numero} não é primo")