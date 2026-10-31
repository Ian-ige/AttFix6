import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dados_pizza.csv")

plt.figure(figsize=(8, 8))
plt.pie(df["faturamento"], labels=df["canal_venda"], autopct="%1.1f%%", startangle=90)
plt.title("Faturamento por Canal de Venda")
plt.tight_layout()
plt.savefig("08_pizza.png", dpi=300)
plt.show()
