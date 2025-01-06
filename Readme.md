# Population Distribution Analysis in France

## Project Overview
This project focuses on analyzing the population distribution in France based on data provided by the **INSEE (Institut National de la Statistique et des Études Économiques)**. It uses a data pipeline inspired by the **Medallion Architecture** to process raw data into clean and aggregated datasets for analysis and visualization. The goal is to study population trends and disparities across regions, considering variables such as age, gender, and total population size.

---

## Objectives

1. **Clean and transform raw data**:
   - Remove anomalies and missing values.
   - Filter valid regions and demographic segments.

2. **Analyze population trends**:
   - Study regional population distributions over time.
   - Compare demographic structures (age, gender) across regions and years.

3. **Provide actionable visual insights**:
   - Generate interactive reports and dashboards using Power BI.

---

## Data Sources
The dataset is sourced from the INSEE’s official website: [Estimation de Population]().

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

---

## Data Architecture

### Medallion Architecture: Tables and Data Flow

#### Tables of Data
1. **Table Bronze**: Raw data (`population_bronze`), containing fields such as gender, age, region, etc.
2. **Table Silver**: Cleaned and transformed data (`population_silver`), with filtering and handling of anomalies.
3. **Table Gold**: Aggregated data (`population_gold`), including indicators like total population and percentage distribution.

#### Data Flow
1. **Bronze**: Import raw data into a MariaDB database.
2. **Silver**: Clean and transform the data by:
   - Removing invalid or unknown values (_T) for AGE and SEX.
   - Filtering by valid region codes (postal codes).
3. **Gold**: Aggregate and calculate indicators for further analysis:
   - Total population and percentage by region, gender, and year.
   - Labels for improved readability.

---

## Methodology

### Step 1: Data Collection
- **Source**: Data was downloaded directly from INSEE’s open data portal.
- **Format**: Files are available in CSV format for easy processing.

### Step 2: Data Cleaning
- Verify column names, types, and completeness of the dataset.
- Match variable codes in `data.csv` with their descriptions in `metadata.csv`.
- Handle missing or invalid data (e.g., remove unnecessary columns or fix formatting).

### Step 3: Data Modeling
- **Fact Table**: Population indicators from `data.csv`.
- **Dimension Tables**: Regions, age groups, and gender from `metadata.csv`.

### Step 4: Data Transformation
- Filter, aggregate, and normalize the data into the Silver and Gold stages:
  - **Silver**: Clean data and remove anomalies.
  - **Gold**: Aggregate data into indicators for analysis.

### Step 5: Visualization
- Use Power BI to create interactive visualizations such as:
  - Regional population density maps.
  - Age and gender distribution histograms.
  - Time-series trend analysis (1990 - 2024).

---

## Tools and Technologies

### Data Ingestion
- Raw CSV files from INSEE.

### Data Processing
- **Python**: Pandas, NumPy for data manipulation.
- **SQL**: MariaDB for database management.

### Data Visualization
- **Power BI**: Interactive dashboards and reports.
- **Python Libraries**: Matplotlib, Seaborn for custom charts.

### Data Architecture
- **Bronze folder**: Raw data storage.
- **Medallion schema**: Structured data processing.

---

## Visualizations in Power BI

1. **Analysis of Men in 1990 (Region 01)**:
   - **Type**: Bar chart.
   - **Axes**: GEO (X), total_population (Y).
   - **Filters**: TIME_PERIOD = 1990, SEX = 'M', GEO = '01'.

2. **Women in Region 01**:
   - **Type**: Stacked column chart.
   - **Axes**: TIME_PERIOD (X), total_population (Y).
   - **Filters**: SEX = 'F', GEO = '01'.

3. **Geographical Distribution**:
   - **Type**: Map.
   - **Location**: GEO.
   - **Size**: total_population.

4. **Dynamic Pivot Tables**:
   - Analyze population by:
     - Region (GEO).
     - Gender (SEX).
     - Year (TIME_PERIOD).

---

## Expected Outcomes

1. **Dynamic Reports**:
   - Visualizations for gender and age analysis.
   - Interactive dashboards for regional comparisons.

2. **Key Insights**:
   - Population trends from 1990 to 2024.
   - Regional disparities and demographic changes.

3. **Reusable Data Structure**:
   - A structured Data Warehouse ready for further analysis.

---

## Future Improvements

- Add predictive analysis based on historical trends.
- Integrate additional data dimensions (e.g., economy, education).
- Automate data updates via APIs.

---

## How to Run the Project

1. **Prepare the Environment**:
   - Install required Python libraries (`pandas`, `matplotlib`, `seaborn`).
   - Set up a MariaDB database.

2. **Load the Data**:
   - Place the raw data in the Bronze folder.
   - Run provided scripts to clean and load the data into Silver and Gold tables.

3. **Run Analysis**:
   - Use Jupyter Notebook or SQL scripts for exploratory data analysis (EDA).

4. **Generate Visualizations**:
   - Load the Gold table into Power BI to create reports.

---

## References
- [INSEE Official Website](https://www.insee.fr)