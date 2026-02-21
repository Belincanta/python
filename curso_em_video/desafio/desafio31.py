# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
km = int(input('Digite quantos KM você fez: '))
if km <= 200:
    print(f'Seja bem vindo novamente! Você percorreu {km}km ao total, gastando o valor de R$ {km*0.5:.2f}')
else:
    print(f'Seja bem vindo novamente! Você percorreu {km}km ao total, gastando o valor de R${km*0.45:.2f}, economizando ao todo certo de R${(km*0.5) - (km*0.45):.2f} devido ter percorrido mais que 200km')