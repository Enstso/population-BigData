import pandas as pd
from sqlalchemy import create_engine, text
import os

# Chargement des fichiers CSV
print(os.getcwd())
data = pd.read_csv("../../data/bronze/data.csv", sep=";")
metadata = pd.read_csv("../../data/bronze/metadata.csv", sep=";")

# Filtrer les données définitives ("D")
definitive_data = data[data["OBS_STATUS_FR"] == "D"].copy()

# Nettoyer et typer les colonnes
definitive_data["OBS_VALUE"] = definitive_data["OBS_VALUE"].round().astype(int)  # Typage en entier
definitive_data["TIME_PERIOD"] = definitive_data["TIME_PERIOD"].astype(int)  # Typage en entier
for col in ["GEO", "GEO_OBJECT", "SEX", "AGE", "EP_MEASURE", "OBS_STATUS_FR"]:
    definitive_data[col] = definitive_data[col].astype(str)

# Connexion à la base MariaDB
user = os.getenv("DB_USER", "user")
password = os.getenv("DB_PASSWORD", "user_password")
engine = create_engine(f"mysql+pymysql://{user}:{password}@127.0.0.1:3306/population_db")

# Créer la table si elle n'existe pas
create_table_query = """
CREATE TABLE IF NOT EXISTS population_bronze (
    GEO VARCHAR(10) NOT NULL,
    GEO_OBJECT VARCHAR(10) NOT NULL,
    SEX CHAR(1) NOT NULL,
    AGE VARCHAR(20) NOT NULL,
    EP_MEASURE VARCHAR(10) NOT NULL,
    OBS_STATUS_FR CHAR(1) NOT NULL CHECK (OBS_STATUS_FR = 'D'),
    TIME_PERIOD YEAR NOT NULL CHECK (TIME_PERIOD BETWEEN 1900 AND 2100),
    OBS_VALUE INT NOT NULL CHECK (OBS_VALUE >= 0),
    PRIMARY KEY (GEO, TIME_PERIOD, SEX, AGE, EP_MEASURE)
);
"""
try:
    with engine.connect() as connection:
        connection.execute(text(create_table_query))
        definitive_data.to_sql("population_bronze", con=engine, if_exists="replace", index=False)
        print("Données insérées avec succès.")
except Exception as e:
    print(f"Erreur lors de l'insertion des données : {e}")
