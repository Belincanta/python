# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros
v = int(input('Digite um valor: '))
c = v * 100
m = v * 1000
print('O valor digitado é {} metros, possui {} centímetros e {} milímetros'.format(v, c, m))