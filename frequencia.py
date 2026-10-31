import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dados_frequencia.csv")

frequencia = df["tipo_atendimento"].value_counts()

plt.figure(figsize=(10, 6))
frequencia.plot(kind="bar")
plt.title("Frequência por Tipo de Atendimento")
plt.xlabel("Tipo de Atendimento")
plt.ylabel("Quantidade de Chamados")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("05_frequencia.png", dpi=300)
plt.show()
