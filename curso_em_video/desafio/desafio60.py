# Faça um programa que leia um número qualquer e mostre o seu fatorial. 
# Exemplo:
#5! = 5 x 4 x 3 x 2 x 1 = 120

numero = int(input("Digite um número para calcular o fatorial: "))
c = numero
fatorial = 1
print(f"O fatorial de {numero}! = ", end ="")
while c > 0:
    print(f"{c}", end ="")    
    print(" x " if c > 1 else " = ", end = "")
    fatorial *= c
    c -=1    
print(fatorial)