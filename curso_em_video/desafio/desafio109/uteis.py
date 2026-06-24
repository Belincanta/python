def dobro(v = 0, formatado = False):
    res = v*2
    return res if formatado is False else moeda(res) #retorna o valor sem formatação quando o parâmetro 'formatado' for false ou não existir, passando True virá formatado.

def metade(v = 0, formatado = False):
    res = v/2
    return res if formatado is False else moeda(res)

def aumentar(v = 0, taxa = 0, formatado = False):
    res = v + (v*taxa/100)
    return res if formatado is False else moeda(res)

def diminuir(v = 0, taxa = 0, formatado = False):
    res = v - (v*taxa/100)
    return res if formatado is False else moeda(res)

def moeda(v = 0, moeda = "R$"):
    return f"{moeda} {v:.2f}".replace(".",",")


