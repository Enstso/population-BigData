CREATE TABLE IF NOT EXISTS population_bronze (
    GEO VARCHAR(10) NOT NULL,                              -- Code de la géographie (ex: code de la région, du pays)
    GEO_OBJECT VARCHAR(10) NOT NULL,                        -- Code de l'objet géographique (ex: ID d'une zone géographique spécifique)
    SEX CHAR(1) NOT NULL,                                   -- Sexe de la population (M ou F)
    AGE VARCHAR(20) NOT NULL,                               -- Tranche d'âge (par ex: Y_LT20, Y20T39, etc.)
    EP_MEASURE VARCHAR(10) NOT NULL,                        -- Mesure de la population (ex: POP)
    OBS_STATUS_FR CHAR(1) NOT NULL CHECK (OBS_STATUS_FR = 'D'), -- Statut de l'observation (D pour définitif)
    TIME_PERIOD YEAR NOT NULL CHECK (TIME_PERIOD BETWEEN 1900 AND 2100), -- Période de l'observation (année)
    OBS_VALUE INT NOT NULL CHECK (OBS_VALUE >= 0),         -- Valeur de la population (doit être positive ou égale à 0)
    PRIMARY KEY (GEO, TIME_PERIOD, SEX, AGE, EP_MEASURE)    -- Clé primaire composée de plusieurs colonnes
);



CREATE TABLE IF NOT EXISTS population_silver (
    GEO VARCHAR(10) NOT NULL,                           -- Code de la région ou géographie
    SEX CHAR(1) NOT NULL,                                -- Sexe de la population
    AGE VARCHAR(20) NOT NULL,                           -- Tranche d'âge (ex: Y_LT20, Y20T39, etc.)
    TIME_PERIOD YEAR NOT NULL CHECK (TIME_PERIOD BETWEEN 1900 AND 2100),  -- Année de la période
    OBS_VALUE INT NOT NULL CHECK (OBS_VALUE >= 0),      -- Population (valeur entière)
    POPULATION_PERCENT FLOAT NOT NULL CHECK (POPULATION_PERCENT >= 0),  -- Pourcentage de la population
    PRIMARY KEY (GEO, SEX, AGE, TIME_PERIOD)            -- Clé primaire sur les colonnes géo, sexe, âge, période
);


CREATE TABLE IF NOT EXISTS population_gold (
    GEO VARCHAR(10) NOT NULL,
    SEX CHAR(1) NOT NULL,
    TIME_PERIOD YEAR NOT NULL,
    total_population INT NOT NULL,
    population_percent FLOAT NOT NULL,
    sex_label VARCHAR(10) NOT NULL,
    PRIMARY KEY (GEO, SEX, TIME_PERIOD)
);