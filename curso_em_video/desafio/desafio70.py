# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
total = maismil = menor = cont = 0
produto_barato = " "

while True:
    print("="*15, "LOJÃO DA ECONOMIA", "="*15)
    produto = input("Produto: ")
    valor = float(input("Valor R$ "))
    cont += 1
    total += valor
    if valor > 1000:
        maismil += 1
    if cont == 1 or valor < menor:
        menor = valor
        produto_barato = produto       
    opcao = " "
    while opcao not in "SN":
        opcao = input("Cadastrar outro produto? [S/N]: ").strip().upper()[0]
    if opcao == "N":
        break
print("="*15, "FIM DAS COMPRAS", "="*15)
print(f"""O valor total gasto das compras é de R$ {total:.2f}.
Dos produtos adquiridos, {maismil} custaram mais de mil reais.
O produto mais barato é o {produto_barato}, que custa R$ {menor:.2f}.""")