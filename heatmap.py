import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dados_heatmap.csv")

tabela = df.pivot(index="dia_semana", columns="horario", values="movimento_clientes")
ordem_dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
tabela = tabela.reindex([dia for dia in ordem_dias if dia in tabela.index])

plt.figure(figsize=(10, 6))
plt.imshow(tabela.values, aspect="auto")
plt.colorbar(label="Movimento de Clientes")
plt.xticks(range(len(tabela.columns)), tabela.columns)
plt.yticks(range(len(tabela.index)), tabela.index)
plt.title("Movimento de Clientes por Dia e Horário")
plt.xlabel("Horário")
plt.ylabel("Dia da Semana")
plt.tight_layout()
plt.savefig("06_heatmap.png", dpi=300)
plt.show()
