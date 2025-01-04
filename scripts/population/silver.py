import pandas as pd
from sqlalchemy import create_engine, text

# Connexion à la base MariaDB
engine = create_engine("mysql+pymysql://user:user_password@127.0.0.1:3306/population_db")

# Créer la table population_silver si elle n'existe pas
create_table_query = """
CREATE TABLE IF NOT EXISTS population_silver (
    GEO VARCHAR(10) NOT NULL,
    SEX CHAR(1) NOT NULL,
    AGE VARCHAR(20) NOT NULL,
    TIME_PERIOD YEAR NOT NULL CHECK (TIME_PERIOD BETWEEN 1900 AND 2100),
    OBS_VALUE INT NOT NULL CHECK (OBS_VALUE >= 0),
    POPULATION_PERCENT FLOAT NOT NULL CHECK (POPULATION_PERCENT >= 0),
    PRIMARY KEY (GEO, SEX, AGE, TIME_PERIOD)
);
"""

# Liste des codes postaux français
codes_postaux_fr = [
    "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", 
    "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", 
    "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", 
    "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", 
    "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", 
    "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", 
    "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", 
    "71", "72", "73", "74", "75", "76", "77", "78", "79", "80", 
    "81", "82", "83", "84", "85", "86", "87", "88", "89", "90", 
    "91", "92", "93", "94", "95", "97", "971", "972", "973", "974", 
    "976", "977", "978", "979", "981", "982", "983", "984", "985", 
    "986", "987", "988", "989"
]

try:
    with engine.connect() as connection:
        # Création de la table si elle n'existe pas
        connection.execute(text(create_table_query))
        
        # Charger les données brutes (bronze) depuis la base de données
        query = "SELECT * FROM population_bronze"
        bronze_data = pd.read_sql(query, con=engine)

        # Nettoyage et transformation
        silver_data = bronze_data.copy()

        # Suppression des tranches d'âge et sexe inconnus
        silver_data = silver_data[silver_data["AGE"] != "_T"]
        silver_data = silver_data[silver_data["SEX"] != "_T"]
        
        # Filtrage des régions selon les codes postaux valides (codes de région)
        silver_data = silver_data[silver_data["GEO"].isin(codes_postaux_fr)]
        
        # Calcul de la population totale par région et sexe
        aggregated_data = silver_data.groupby(["GEO", "SEX", "TIME_PERIOD"], as_index=False)["OBS_VALUE"].sum()

        # Ajout de colonnes dérivées
        aggregated_data["POPULATION_PERCENT"] = (
            aggregated_data["OBS_VALUE"] / aggregated_data["OBS_VALUE"].sum() * 100
        )

        # Enregistrer dans la table population_silver
        aggregated_data.to_sql("population_silver", con=engine, if_exists="replace", index=False)

        print("Données silver insérées avec succès dans la base MariaDB.")
except Exception as e:
    print(f"Erreur lors de l'insertion des données : {e}")
