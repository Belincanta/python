#Faça um programa que leia nome e peso de várias pessoas,                                   guardando tudo em uma lista. No final, mostre: 
# A) Quantas pessoas foram cadastradas. 
# B) Uma listagem com as pessoas mais pesadas. 
# C) Uma listagem com as pessoas mais leves.

temp = []
principal = []
maior = menor = 0
while True:
    temp.append(input("Nome: "))    
    temp.append(float(input("Peso: ")))    
    if len(principal) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    principal.append(temp[:])
    temp.clear() #para não repitir os dados
    opcao = " "
    while opcao not in "SN":
        opcao = input("Quer continuar? S/N: ").upper().strip()[0]
    if opcao == "N":
        break
print(f"Os dados digitados foram {principal}")
print(f"Foram cadastras {len(principal)} pessoas ao todo.")
print(f"O peso maior foi de {maior}kg, do(a) ", end="")
for p in principal:
    if p[1] == maior:
        print(f"({p[0]})! ", end="")
print()
print(f"O peso menor foi de {menor}kg, do(a) ", end="")
for p in principal:
    if p[1] == menor:
        print(f"({p[0]})! ", end="")