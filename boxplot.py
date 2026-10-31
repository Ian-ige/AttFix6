import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dados_boxplot.csv")

dados = [grupo["salario"].values for _, grupo in df.groupby("departamento")]
labels = list(df.groupby("departamento").groups.keys())

plt.figure(figsize=(10, 6))
plt.boxplot(dados, labels=labels)
plt.title("Distribuição dos Salários por Departamento")
plt.xlabel("Departamento")
plt.ylabel("Salário")
plt.tight_layout()
plt.savefig("02_boxplot.png", dpi=300)
plt.show()
