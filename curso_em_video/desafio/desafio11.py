# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais foi alugado. Calcule o preço a pagar, sabendo que o carro custo R$60 por dia e R$0,15 por km rodado

dia = int(input('Quantos dias o carro foi utilizado? '))
km = float(input('Nesse período, quantos KM foram percorridos? '))
print(f'O veículo foi utilizado por {dia} dias.')
print(f'Neste período a distância percorrida foi de {km}km.')
print(f'o custo total do aluguel foi de R${(dia*60) + (km*0.15):.2f}')