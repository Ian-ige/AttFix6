import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dados_dispersao.csv")

plt.figure(figsize=(10, 6))
for sexo, grupo in df.groupby("sexo"):
    plt.scatter(grupo["altura_cm"], grupo["peso_kg"], label=sexo, alpha=0.7)
plt.title("Relação entre Altura e Peso")
plt.xlabel("Altura (cm)")
plt.ylabel("Peso (kg)")
plt.legend()
plt.tight_layout()
plt.savefig("03_dispersao.png", dpi=300)
plt.show()
