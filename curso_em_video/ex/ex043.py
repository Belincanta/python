# modularização

def fatorial(n):
    f = 1
    for c in range(1, n+1):
        f*=c
    return f


#programa principal
num = int(input("Digite um número: "))
fat = fatorial(num)
print(f"O fatoral do número {num} é {fat}")