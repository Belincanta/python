#Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

def dobro(p):
    return p * 2

def metade(p):
    return p / 2

def aumentar(p):
    return p + (p * 0.10)

def diminuir(p):
    return p - (p * 0.10)