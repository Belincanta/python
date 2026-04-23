# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = ("Lápis", 1.75,
            "Borracha", 3.75,
            "Lapiseira", 7.50,
            "Lápis de Cor", 23.50,
            "Apontador", 5.50,
            "Estojo", 12.00,
            "Caderno", 23.99,
            "Folha A4", 21.10,
            "Mochila", 75.90)
print("-"*40)
print(f"{'LISTAGEM DE PREÇOS':^40}")
print("-"*40)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f"{produtos[pos]:.<30}", end=" ")
    else:
        print(f"R${produtos[pos]:>7.2f}")
print("-"*40)