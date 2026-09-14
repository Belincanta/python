from rich import print

class Caneta:
    def __init__(self, cor = "azul"):
        escolha = ""
        match cor.lower().strip(): #match é como o if
            case "azul": #se for azul
                escolha = "[blue]"
            case "vermelho" | "vermelha": # se for vermelho ou vermelha
                escolha = "[red]"
            case "verde": #se for verde
                escolha = "[green]"
            case _: #se for diferente de tudo
                escolha = "[white]"
        self.cor = escolha
        self.tampada = True

    def escrever(self, msg):
        if self.tampada:
            print(f":prohibited: A {self.cor}caneta [/]está tampada!")
        else:
            print(f"{self.cor}{msg}[/]", end="")

    def pular_linha(self, qtde = 1):
        print(f"\n" * qtde, end="")

    def tampar(self):
        self.tampada = True

    def destampar(self):
        self.tampada = False

#declaração dos objetos
c1 = Caneta("azul")
c2 = Caneta("vermelho")
c3 = Caneta("verde")
c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever("Olá mundo")
c2.pular_linha(3)
c2.escrever("Vermelho")
c3.pular_linha(1)
c3.escrever("palmeiras")
