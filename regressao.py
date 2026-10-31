import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("dados_regressao.csv")

x = df["renda_mensal"]
y = df["gasto_mensal"]
coeficientes = np.polyfit(x, y, 1)
reta = np.poly1d(coeficientes)
x_linha = np.linspace(x.min(), x.max(), 100)

plt.figure(figsize=(10, 6))
plt.scatter(x, y, label="Dados")
plt.plot(x_linha, reta(x_linha), label="Regressão Linear")
plt.title("Regressão Linear entre Renda e Gasto Mensal")
plt.xlabel("Renda Mensal")
plt.ylabel("Gasto Mensal")
plt.legend()
plt.tight_layout()
plt.savefig("09_regressao.png", dpi=300)
plt.show()
