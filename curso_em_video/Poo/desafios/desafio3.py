from rich import print
from rich.panel import Panel

# criação da classe

class Churrasco:
    #atrinuto de chasse
    consumo_padrao:float = 0.400 #400g por pessoa
    preco_kg:float = 82.40 #valor por kg

    def __init__(self, titulo, quant):
        #atributos de instância
        self.titulo = titulo
        self.participantes = quant

    def __str__(self):
        return f"Esse é o {self.titulo} com {self.participantes} pessoas envolvidas."

    def calcular_qtde_carne(self) -> float:
        return self.participantes * Churrasco.consumo_padrao

    def calcular_custo_total(self) -> float:
        return self.calcular_qtde_carne() * Churrasco.preco_kg

    def calcular_custo_individual(self) -> float:
        return self.calcular_custo_total() / self.participantes

    def analisar(self):
        conteudo = f"Analizando {self.titulo} com {self.participantes} convidados."
        conteudo += f"\nCada participante comerá {Churrasco.consumo_padrao}kg e custará R${Churrasco.preco_kg:.2f} por kg."
        conteudo += f"\nRecomendo comprar {self.calcular_qtde_carne():.3f} kg de carne."
        conteudo += f"\nO custo total será R${self.calcular_custo_total():.2f}."
        conteudo += f"\nCada participante gastará R${self.calcular_custo_individual():.2f}."
        Painel = Panel(conteudo, title=self.titulo)
        print(Painel)

#declaração dos objetos
c1 = Churrasco(titulo="Churras dos amigos", quant=15)
c1.analisar()

c2 = Churrasco(titulo="Churras da firma", quant=9)
c2.analisar()


    