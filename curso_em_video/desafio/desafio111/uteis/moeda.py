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

def resumo(v = 0, taxa_au = 10, taxa_di = 5):
    print("-" * 30)
    print(f"Resumo do valor".center(30))
    print("-" * 30)
    print(f"Analisando o preço: \t{moeda(v)}")
    print(f"O dobro é \t\t{dobro(v, True)}")
    print(f"A metade é \t\t{metade(v, True)}")
    print(f"{taxa_au}% de aumento é \t{aumentar(v, taxa_au, True)}")
    print(f"{taxa_di}% de redução é \t{diminuir(v, taxa_di, True)}")
    print("-" * 30)
