# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ("ATENCAO", "PALMEIRAS", "JOGADOR", "CAMPEAO", "VERDAO", "PROGRAMACAO", "PYTHON", "CURSO", "FAMILIA", "RESPEITO", "DISCIPLINA", "CONSTANCIA", "PAZ")
for p in palavras:    
    print(f"\nNa palavra '{p}' possui as vogais >>>", end=" ")
    for letras in p:
        if letras in "AEIOU":
                print(f"{letras}", end=" ")
