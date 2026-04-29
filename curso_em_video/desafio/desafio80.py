# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
numeros = list()
for c in range(0, 5):
    n = (int(input("Digite um número: ")))
    if c == 0 or n > numeros[-1]: # se for o primeiro número, vai para o final da fila ou se o número for maior que o último, vai para o final da fila
        numeros.append(n)
        print("Número adicionado no final da lista...")
    else:
        pos = 0
        while pos < len(numeros): # enquanto o número for menor que as posições da lista
            if n <= numeros[pos]: # se o número que eu quero inserir é menor ou igual a ele
                numeros.insert(pos, n)
                print(f"Número adicionado na posição {pos} da lista...")
                break
            pos += 1 
print(f"Você digitou os números {numeros}")