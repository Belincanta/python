# Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

# criando uma matriz 3x3
matriz = [[0,0,0], [0,0,0], [0,0,0]]

# inputando os valores na linha e nas colunas
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f"Digite um número [{l}, {c}] "))

# printando esses valores nas suas posições
for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz [l][c]:^3}]", end="") # 3 casas decimais e centralizado
    print()