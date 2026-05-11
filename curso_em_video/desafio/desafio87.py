# Aprimore o desafio anterior, mostrando no final:                                                    A) A soma de todos os valores pares digitados.                                                                                                  B) A soma dos valores da terceira coluna.                                                                                                                C) O maior valor da segunda linha.

soma_par = soma_3_col = maior_2_lin = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f"Digite um número | [{l}, {c}]: "))
        if matriz[l][c] % 2 == 0:
            soma_par += matriz[l][c]
for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]:^3}]", end="")
    print()
print(f"A soma de todos os valores pares são {soma_par}")
for l in range(0,3):
    soma_3_col += matriz[l][2]
print(f"A soma da terceira coluna é {soma_3_col}")
for c in range(0,3):
    if c == 0:
        maior_2_lin = matriz[1][c]
        if matriz[1][c] > maior_2_lin:
            maior_2_lin = matriz[1][c]
print(f"O maior valor da 2 coluna é {maior_2_lin}")
