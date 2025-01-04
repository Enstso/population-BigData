# Population Distribution Analysis in France

## Project Overview
This project focuses on analyzing the population distribution in France based on data provided by the **INSEE (Institut National de la Statistique et des Études Économiques)**. The goal is to study population trends and disparities across regions, considering variables such as age, gender, and total population size.

## Objectives
1. **Understand regional population distribution**: Identify areas with high or low population density.
2. **Analyze demographic structures**: Examine the breakdown of populations by age groups and gender.
3. **Provide insights for visualization**: Use data to create visualizations highlighting key demographic patterns.

---

## Data Sources
The dataset is sourced from the INSEE’s official website: [Estimations de population](https://www.insee.fr/fr/statistiques/6008693?sommaire=6008495). This dataset provides estimations of population indicators at the departmental, regional, and national levels.

### Dataset Details
- **Title**: Estimations de population
- **Description**: Contains data on the population as of January 1st, including breakdowns by sex and age groups, average and median age by sex, and the proportion of the population aged 65 and older compared to the population aged 20 to 65.
- **Identifier**: DS_ESTIMATION_POPULATION
- **Theme**: Population trends and structure
- **Period**: 1990 - 2024
- **Variables**: 5 (referenced in `metadata.csv`)
- **Number of Rows**: 264,951 (in `data.csv`)
- **Source**: INSEE’s population estimations
- **License**: Open License
- **Frequency**: Annual


## CSV Files Breakdown

1. data.csv:
    - Columns:
        GEO: Geographic identifier (region, department, or national level).
        - GEO_OBJECT: Geographic description (name of the region or department).
        - SEX: Gender (e.g., M for Male, F for Female).
        - AGE: Age group.
        - EP_MEASURE: Estimation parameter.
        - OBS_STATUS_FR: Observation status (e.g., validated, estimated).
        - TIME_PERIOD: Year of observation.
        - OBS_VALUE: Population value.

- Rows: Contains population data across years (1990-2024).

2. metadata.csv:
    - Columns:
        - COD_VAR: Code for each variable.
        - LIB_VAR: Description of each variable.
        - COD_MOD: Code for each modality (e.g., AGE or SEX).
        - LIB_MOD: Description of each modality.

## Methodology

### Step 1: Data Collection

- Source: Data was downloaded directly from INSEE’s open data portal.
- Format: Files are available in CSV format for easy processing.

### Step 2: Data Cleaning

- Verify column names, types, and completeness of the dataset.*
- Match variable codes in data.csv with their descriptions in metadata.csv.
- Handle missing or invalid data (e.g., remove unnecessary columns or fix formatting).

### Step 3: Data Modeling

- Develop a star schema for organizing the data into a structured Data Warehouse format:
    - Fact Table: Population indicators from data.csv.
    - Dimension Tables: Regions, age groups, and gender from metadata.csv.

### Step 4: Data Transformation

- Perform transformations such as filtering, aggregation, and normalization to prepare the data for analysis.

### Step 5: Visualization

- Generate insightful visualizations using tools like Power BI, Apache Superset, or Python libraries such as Matplotlib or Seaborn. Example visualizations include:

    - Regional population density maps.
    - Age and gender distribution histograms.
    - Trend analysis over time (1990 - 2024).


## Tools and Technologies

1. **Data Ingestion**:
    - Raw CSV files from INSEE.

2. **Data Processing:**:
    - Python (Pandas, NumPy).
    - SQL for transformations.

3. **Data Visualization**:
    - Power BI or Apache Superset.
    - Python (Matplotlib, Seaborn).

4. **Data Architecture**:
    - Bronze folder (raw data).
    - Star schema for the Data Warehouse.

## Expected Outcomes

1. A detailed report highlighting:

    - Regional population distributions.

    - Insights on age and gender demographics.

    - Analysis of trends over the years 1990 - 2024.

2. Visualizations showcasing:

    - Population trends.

    - Disparities across regions.

    - Changes in age demographics.

3. A structured Data Warehouse to facilitate further analysis.

## How to Run the Project

1. Prepare the Environment:

    - Install required Python libraries: pandas, matplotlib, seaborn.

    - Set up a database for structured data (e.g., PostgreSQL, SQLite).

2. Load the Data:

    - Place the raw data in the bronze folder.

    - Use provided Python scripts to clean and load the data into the database.

3. Run Analysis:

    - Use Jupyter Notebook or SQL scripts to perform exploratory data analysis (EDA).

4. Generate Visualizations:

    - Open the Power BI file or run visualization scripts to generate charts and maps.


## Authors

This project is carried out by a team of 4 students as part of the DP-203 Data Engineering course. Contributions include:

- Data collection and cleaning.
- Data modeling and transformation.
- Visualization and reporting.

## References

- INSEE Official Website: https://www.insee.fr
- Population Dataset: Estimations de population

