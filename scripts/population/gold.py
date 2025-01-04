import pandas as pd
from sqlalchemy import create_engine, text

# Connexion à la base MariaDB
engine = create_engine("mysql+pymysql://user:user_password@127.0.0.1:3306/population_db")

# Charger les données depuis la table population_silver
query = "SELECT * FROM population_silver"
silver_data = pd.read_sql(query, con=engine)

# Nettoyage ou transformations supplémentaires si nécessaire
# Agrégations par géo, sexe et période pour obtenir la population totale
gold_data = silver_data.groupby(["GEO", "SEX", "TIME_PERIOD"], as_index=False).agg(
    total_population=pd.NamedAgg(column="OBS_VALUE", aggfunc="sum"),
    # Ajouter des agrégations supplémentaires comme le pourcentage de la population
    population_percent=pd.NamedAgg(column="OBS_VALUE", aggfunc=lambda x: (x.sum() / silver_data["OBS_VALUE"].sum()) * 100)
)

# Ajouter des informations supplémentaires comme des labels lisibles pour le sexe
gold_data['sex_label'] = gold_data['SEX'].map({'M': 'Male', 'F': 'Female'})

# Créer la table 'population_gold' si elle n'existe pas déjà
create_table_query = """
CREATE TABLE IF NOT EXISTS population_gold (
    GEO VARCHAR(10) NOT NULL,
    SEX CHAR(1) NOT NULL,
    TIME_PERIOD YEAR NOT NULL,
    total_population INT NOT NULL,
    population_percent FLOAT NOT NULL,
    sex_label VARCHAR(10) NOT NULL,
    PRIMARY KEY (GEO, SEX, TIME_PERIOD)
);
"""

# Exécuter la requête de création de la table
with engine.connect() as connection:
    connection.execute(text(create_table_query))

# Insérer les données dans la table population_gold
gold_data.to_sql("population_gold", con=engine, if_exists="replace", index=False)

print("Données Gold insérées avec succès dans la base MariaDB.")
