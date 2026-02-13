n1 = float(input('Digite uma nota: '))
n2 = float(input('Digite outra nota: '))
media = (n1+n2)/2
print(f'Sua média é {media:.1f}')
if media >= 6.0:
    print('Parabéns, você passou!')
else:
    print('Você foi reprovado, estude mais.')