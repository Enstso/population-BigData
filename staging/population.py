import pandas as pd

# Chargement des fichiers CSV
data = pd.read_csv("./data/bronze/data.csv", sep=";")
metadata = pd.read_csv("./data/bronze/metadata.csv", sep=";")

# Filtrer les données définitives ("D")
definitive_data = data[data["OBS_STATUS_FR"] == "D"].copy()  # Utilisation de .copy() pour éviter les avertissements.

# Arrondir les valeurs en entier
definitive_data["OBS_VALUE"] = definitive_data["OBS_VALUE"].round().astype(int)

# Fonction pour analyser la population par groupe d'âge et sexe
def analyze_by_age_and_sex():
    grouped_data = definitive_data[
        definitive_data["EP_MEASURE"] == "POP"
    ].groupby(["SEX", "AGE"])["OBS_VALUE"].sum().reset_index()

    # Réorganisation des données pour une meilleure lisibilité
    pivot_data = grouped_data.pivot(index="AGE", columns="SEX", values="OBS_VALUE")

    return pivot_data

# Analyser la population
analysis_result = analyze_by_age_and_sex()

# Afficher les résultats
print("Analyse de la population par groupe d'âge et sexe :\n")
print(analysis_result)

