# Docstring

def contador(i, f, p):
    """
    i = inicio da contagem
    f = fim da contagem
    p = passo da contagem, pular em x números a contagem
    """
    c = i
    while c <= f:
        print(f"{c} > ", end="")
        c += p
    print("FIM!")


# programa principal
contador(2, 20, 2)

help(contador)