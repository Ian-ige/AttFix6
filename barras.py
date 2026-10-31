import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dados_barras.csv")

pivot = df.pivot(index="categoria", columns="regiao", values="vendas_medias")
ax = pivot.plot(kind="bar", figsize=(10, 6))
ax.set_title("Vendas Médias por Categoria e Região")
ax.set_xlabel("Categoria")
ax.set_ylabel("Vendas Médias")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("01_barras.png", dpi=300)
plt.show()
