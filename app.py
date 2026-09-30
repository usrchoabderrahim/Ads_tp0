import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Test rapide des bibliothèques installées
data = {
    'Categories': ['A', 'B', 'C', 'D'],
    'Valeurs': [10, 20, 15, 25]
}

df = pd.DataFrame(data)

# 2. Génération d’un graphique de validation
sns.set_theme(style="darkgrid")

sns.barplot(x="Categories", y="Valeurs", data=df)

plt.title("Validation de l'environnement uv")
plt.show()