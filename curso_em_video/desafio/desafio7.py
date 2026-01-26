# Faça um programa que leia a largura e a altura de uma parede em metros, calcula a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta 2 quadrados
alt = float(input('Digite a altura: '))
lar = float(input('Digite a largura: '))
print(f'A area da sua parede é de {alt*lar} metros')
print(f'Você vai precisar de {(alt*lar)/2:.0f} litros para pintar esta parede completa, utilizando a nossa tinta.')