# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

#função passando parametros larg e alt que é igual a largura e altura no programa principal
def area(larg, alt): 
    a = larg * alt
    print(f"Com altura de {alt}m2 e com largura de {larg}m2, temos a área de {a}m2")

    
# programa principal
print("="*10)
print("CALCULANDO AREAS")
print("="*10)
largura = float(input("Digite a largura m2: "))
altura = float(input("Digite a altura m2: "))
area(largura, altura)


