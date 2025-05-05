import numpy as np
import matplotlib.pyplot as plt

# 1. Loeme andmed failist
nimed = []
korgused = []

with open("maed.txt", "r") as fail:
    for rida in fail:
        osad = rida.strip().split()
        nimi = " ".join(osad[:-1]).replace("_", " ")
        korgus = int(osad[-1])
        nimed.append(nimi)
        korgused.append(korgus)

# 2. Kasutame NumPy'd
korgused_np = np.array(korgused)

keskmine = np.mean(korgused_np)
max_korgus = np.max(korgused_np)
min_korgus = np.min(korgused_np)
summa = np.sum(korgused_np)

# 3. Leiame vastavad mäed
max_index = np.argmax(korgused_np)
min_index = np.argmin(korgused_np)
korgeim_magi = nimed[max_index]
madalaim_magi = nimed[min_index]

# 4. Kuvame tulemused
print("Statistika:")
print(f"Keskmine kõrgus: {keskmine:.2f} m")
print(f"Kõrgeim mägi: {korgeim_magi} ({max_korgus} m)")
print(f"Madalaim mägi: {madalaim_magi} ({min_korgus} m)")
print(f"Kogukõrgus ekspeditsiooniks: {summa} m")

# 5. Visualiseerime matplotlibiga
plt.figure(figsize=(10, 6))
plt.bar(nimed, korgused, color='skyblue')
plt.xlabel("Mäed")
plt.ylabel("Kõrgus (m)")
plt.title("Maailma kõrgeimad mäed")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
