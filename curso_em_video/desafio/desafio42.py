#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#– EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes

print("="*22)
print("Analisador de triangulo")
print("="*22)
r1 = int(input("Digite a primeira reta: "))
r2 = int(input("Digite a segunda reta: "))
r3 = int(input("Digite a terceira reta: "))
if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    print("Os seguimentos podem formar um triangulo", end = " ")
    if r1 == r2 == r3: #todos iguais
        print("EQUILÁTERO")
    elif r1 != r2 != r3 != r1:
        print("ESCALENO")
    else:
        print("ISÓSCELES")
else:
    print("Os elementos não podem forma um triângulo!")

#end = " " é para não pular a linha, fazendo a junção dos dois prints.