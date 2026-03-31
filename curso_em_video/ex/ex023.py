# uso de while

n = 1
par = impar = 0
while n != 0: # enquanto n for diferente de zero, vai continuar perguntando ao usuário.
    n = int(input("Digite um número: "))
    if n != 0: # só cai na condição de par ou impar se for diferente de 0
        if n % 2 == 0:
            par += 1
        else:
            impar +=1    
print(f"Você digitou {par} números pares e {impar} números impares.")
