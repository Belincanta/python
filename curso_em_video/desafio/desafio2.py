# crie um algoritmo que leia um número e mosrte o seu dobro, triplo e raiz quadrada.
n = int(input('Digite um número: '))
d = n*2
t = n*3
r = n**0.5
print('O número digita foi {}, o dobro é {}, o triplo é {} e a raiz quadrada é {:.1f}'.format(n, d, t, r))