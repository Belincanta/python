#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos:
#APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = input("Digite uma frase: ").strip().upper()
palavras = frase.split() #separo as letras
junto = "".join(palavras) #faço a junção das letras sem espaços
reverso = ""
for letra in range(len(junto) -1, -1, -1): #percorre até a última letra e vem de trás pra frente
    reverso += junto[letra]
print(f"O inverso de '{frase}' é '{reverso}'")
if reverso == junto:
    print("Logo esta frase é um políndromo")
else:
    print("Logo esta frase não é um políndromo")



