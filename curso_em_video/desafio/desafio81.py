# Crie um programa que vai ler vários números e colocar em uma lista.                  Depois disso, mostre: 
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.  
# C) Se o valor 5 foi digitado e está ou não na lista.

numeros = []
while True:
    numeros.append(int(input("Digite um número: ")))
    opcao = " "
    while opcao not in "SN":
        opcao = input("Quer continuar? S/N: ").strip().upper()[0]
    if opcao == "N":
        break
print("="*30)
numeros.sort(reverse = True)
print(f"Fim da contagem... Ao todo foram digitados {len(numeros)} números.")
print(f"A lista ordenada em ordem descente é {numeros}")
if 5 in numeros:
    print("O número 5 foi digitado!")
else:
    print("o número 5 não foi digitado.")
