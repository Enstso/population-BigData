import pandas as pd

# Chargement des fichiers CSV
data = pd.read_csv("../data/bronze/data.csv", sep=";")
metadata = pd.read_csv("../data/bronze/metadata.csv", sep=";")

# Inspection rapide des données
print("Aperçu des données (data.csv) :")
print(data.head())
print("\nAperçu des métadonnées (metadata.csv) :")
print(metadata.head())
