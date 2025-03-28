# 📌 Importation des bibliothèques
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Seaborn est bien installé !")

# 📌 Charger les données depuis une URL (dataset de Our World in Data)
url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
df = pd.read_csv(url)

# 📌 Afficher les premières lignes
print(df.head())

# 📌 Vérifier les dimensions du dataset (nombre de lignes et de colonnes)
print("Dimensions du dataset :", df.shape)

# 📌 Afficher les noms des colonnes disponibles
print("\nNoms des colonnes :", df.columns)

# 📌 Vérifier les types de données et les valeurs manquantes
print("\nInfos sur le dataset :")
print(df.info())

# 📌 Résumé statistique des colonnes numériques
print("\nRésumé statistique :")
print(df.describe()) 

# 📌 Sélectionner seulement les colonnes importantes
colonnes_utiles = ["location", "date", "total_cases", "new_cases", "total_deaths", "new_deaths"]
df = df[colonnes_utiles]

# 📌 Vérifier les valeurs manquantes
print("\nValeurs manquantes par colonne :")
print(df.isnull().sum())

# 📌 Supprimer les lignes où "total_cases" est manquant
df = df.dropna(subset=["total_cases"])

# 📌 Convertir la colonne "date" en format datetime
df["date"] = pd.to_datetime(df["date"])

# 📌 Filtrer un pays (exemple : France)
df_france = df[df["location"] == "France"]

# 📌 Afficher les 5 premières lignes du dataset filtré
print("\nDonnées de la France :")
print(df_france.head())

# 📌 Configurer le style de Seaborn
sns.set_style("darkgrid")

# 📌 Tracer l'évolution des cas de COVID-19 en France
plt.figure(figsize=(12, 6))  # Taille du graphique
sns.lineplot(data=df_france, x="date", y="total_cases", marker="o", color="blue")

# 📌 Ajouter un titre et des labels
plt.title("Évolution des cas de COVID-19 en France", fontsize=14)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Nombre total de cas", fontsize=12)
plt.xticks(rotation=45)  # Rotation des dates pour une meilleure lisibilité

# 📌 Afficher le graphique
plt.show()
