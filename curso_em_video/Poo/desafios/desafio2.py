from rich import print
from rich.panel import Panel

#criação da classe
class Produto:
    """
    Criação de etiquetas dos produtos.
    """
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"O produto {self.nome} custa cerca de {self.preco:.2f}"

    def etiqueta(self):
        conteudo = f"{self.nome.center(30, " ")}"
        conteudo += f"{"-"*30}"
        precof = f"R${self.preco:.2f}"
        conteudo += f"{precof.center(30, ".")}"
        etiqueta = Panel(conteudo, title="Produto", width=34)
        print(etiqueta)

# declaração do objeto
p1 = Produto(nome="Iphone pro max 18", preco=12500)
p2 = Produto(nome="Notebook Acer", preco=4500)
print(p1)
print(p2)
p1.etiqueta()
p2.etiqueta()