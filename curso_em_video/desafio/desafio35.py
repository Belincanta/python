# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print("="*22)
print("Analisador de triangulo")
print("="*22)
r1 = int(input("Digite a primeira reta: "))
r2 = int(input("Digite a segunda reta: "))
r3 = int(input("Digite a terceira reta: "))
if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    print("Os seguimentos podem formar um triangulo")
else:
    print("Os seguimentos não podem formar um triangulo")
    