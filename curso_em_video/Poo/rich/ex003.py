from rich import print
from rich.table import Table

tabela = Table(title="Tabela de precos")

tabela.add_column("Nome")
tabela.add_column("Preço")
tabela.add_row("Detergente", "R$ 1,90")
tabela.add_row("Amaciante", "R$ 39,80")
print(tabela)
