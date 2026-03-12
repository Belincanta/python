#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep
for c in range(10, -1, -1):
    sleep(0.5)
    print(c)
print("BUM! BUM! POW!")

#10 para começar, -1 para chegar no 0, pois se usar o 0 vai ignorar e terminar no 1. O último -1 é para ordem decrescente