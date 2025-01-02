import pandas as pd

# Récupération de la population des hommes, femmes et total en fonction de l'année de l'étude.

# Chargement des fichiers CSV
data = pd.read_csv("./data/bronze/data.csv", sep=";")
metadata = pd.read_csv("./data/bronze/metadata.csv", sep=";")

# Filtrer les données définitives ("D")
definitive_data = data[data["OBS_STATUS_FR"] == "D"].copy()  # Utilisation de .copy() pour éviter les avertissements de modification.

# Arrondir les valeurs en entier
definitive_data["OBS_VALUE"] = definitive_data["OBS_VALUE"].round().astype(int)

# Fonction pour filtrer par sexe
def filter_by_sex(sex_code):
    return definitive_data[
        (definitive_data["SEX"] == sex_code) & (definitive_data["EP_MEASURE"] == "POP")
    ]

# Extraction des données pour hommes, femmes et total
male_population = filter_by_sex("M")
female_population = filter_by_sex("F")
total_population = filter_by_sex("_T")

# Affichage par TIME_PERIOD
for sex, df in [("Hommes", male_population), ("Femmes", female_population), ("Total", total_population)]:
    print(f"\nPopulation ({sex}):")
    print(df.groupby("TIME_PERIOD")["OBS_VALUE"].sum())
