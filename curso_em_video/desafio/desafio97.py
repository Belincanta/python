# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
def escreva(msg):
    tamanho = len(msg) + 4
    print("~" * tamanho)
    print(f" {msg}") #dois espaços antes para centralizar.
    print("~" * tamanho)

# função principal
escreva("Alessandro Belincanta")
escreva("Olá")
escreva("Palmeiras")