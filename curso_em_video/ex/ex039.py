# funções com desempacotador
def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f"Somando os valores {valores} fica {s}")

soma(2, 4, 6, 8)
soma(2, 4, 6)