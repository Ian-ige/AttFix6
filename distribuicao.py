import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dados_distribuicao.csv")

plt.figure(figsize=(10, 6))
plt.hist(df["idade"], bins=10, edgecolor="black")
plt.title("Distribuição das Idades dos Clientes")
plt.xlabel("Idade")
plt.ylabel("Frequência")
plt.tight_layout()
plt.savefig("04_distribuicao.png", dpi=300)
plt.show()
