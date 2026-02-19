# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = int(input('Em que velocidade estava? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido de 80km/h.')
    print(f'Sua multa será de R$ {(velocidade - 80)*7:.2f}')
else:
    print('Tenha um bom dia, dirija com cuidado!')

