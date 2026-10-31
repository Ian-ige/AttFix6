import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dados_linhas.csv")
df["data"] = pd.to_datetime(df["data"])

plt.figure(figsize=(12, 6))
for loja, grupo in df.groupby("loja"):
    grupo = grupo.sort_values("data")
    plt.plot(grupo["data"], grupo["vendas"], label=loja)
plt.title("Vendas ao Longo do Tempo por Loja")
plt.xlabel("Data")
plt.ylabel("Vendas")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("07_linhas.png", dpi=300)
plt.show()
