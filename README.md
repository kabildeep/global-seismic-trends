# Global Seismic Trends: Data-Driven Earthquake Insights

## Project Overview

Global Seismic Trends is a data science project that analyzes earthquake activity around the world from 2021 to 2025.

The project uses earthquake data collected from the USGS Earthquake Hazards Program API. The data is retrieved, cleaned, stored in MySQL, analyzed using SQL, visualized using Python, and presented through an interactive Streamlit dashboard.

## Objective

The main objectives of this project are:

- Collect global earthquake data from the USGS API
- Clean and prepare the earthquake dataset
- Extract useful information such as country, year, month, and day
- Store the cleaned data in MySQL
- Perform SQL-based earthquake analysis
- Create data visualizations using Python
- Build an interactive Streamlit dashboard
- Identify important earthquake patterns and trends

## Technologies Used

- Python
- Pandas
- Requests
- Regular Expressions
- Matplotlib
- Seaborn
- MySQL
- SQLAlchemy
- PyMySQL
- Streamlit
- Jupyter Notebook
- VS Code

## Data Source

The earthquake data was collected from the USGS Earthquake Hazards Program.

The project uses the USGS Earthquake API to retrieve earthquake records for the period from 2021 to 2025.

Minimum earthquake magnitude used for data collection:

```text
Magnitude >= 3
```

## Dataset

The final dataset contains:

- 104,442 earthquake records
- 33 columns after data cleaning
- Data period: 2021 to 2025

Important columns include:

- id
- time
- updated
- latitude
- longitude
- depth_km
- mag
- magType
- place
- status
- tsunami
- sig
- net
- nst
- dmin
- rms
- gap
- country
- year
- month
- day
- day_of_week
- depth_category
- magnitude_category

## Project Workflow

```text
USGS Earthquake API
        ↓
Data Retrieval
        ↓
Data Cleaning
        ↓
Feature Engineering
        ↓
CSV Dataset
        ↓
MySQL Database
        ↓
SQL Analysis
        ↓
Python Visualization
        ↓
Streamlit Dashboard
```

## Data Retrieval

The Python retrieval script connects to the USGS Earthquake API.

The data is retrieved month by month from January 2021 to December 2025.

Error handling is included for:

- Timeout errors
- Connection errors
- HTTP errors
- Request errors
- Invalid response data

The retrieved data is saved as:

```text
global_earthquake_data_2021_2025.csv
```

## Data Cleaning

The cleaning process includes:

- Converting date and time columns
- Converting numeric columns
- Handling missing values
- Extracting country information from the place column
- Creating year and month columns
- Creating day and day-of-week columns
- Creating depth categories
- Creating magnitude categories

The cleaned dataset is saved as:

```text
data/cleaned_earthquake_data_2021_2025.csv
```

## Feature Engineering

Additional columns were created during data cleaning.

### Country

Country information was extracted from the earthquake location.

### Year

The year was extracted from the earthquake time.

### Month

The month was extracted from the earthquake time.

### Day

The day was extracted from the earthquake time.

### Day of Week

The day of the week was created from the earthquake date.

### Depth Category

Earthquakes were classified into:

```text
Shallow
Deep
```

### Magnitude Category

Earthquakes were classified into:

```text
Moderate
Strong
Major
```

## MySQL Database

The cleaned dataset was uploaded to MySQL.

Database:

```text
global_seismic_db
```

Table:

```text
earthquakes
```

Total records stored in MySQL:

```text
104,442
```

Python libraries used for MySQL connection:

```text
SQLAlchemy
PyMySQL
```

## SQL Analysis

SQL was used to answer analytical questions about earthquake activity.

Examples include:

- Top 10 strongest earthquakes
- Top 10 deepest earthquakes
- Shallow earthquakes with high magnitude
- Average magnitude by magnitude type
- Year with the highest number of earthquakes
- Month with the highest number of earthquakes
- Day of week with the highest earthquake activity
- Earthquake count by hour
- Most active reporting network
- Reviewed versus automatic earthquakes
- Earthquake types
- Tsunami events by year
- Countries with high average magnitude
- Shallow versus deep earthquake ratios
- Deep-focus earthquake regions

The SQL queries are stored in:

```text
sql/earthquake_analysis.sql
```

## Python Visualizations

Python and Matplotlib were used to create visualizations for earthquake patterns.

The visualizations include:

1. Earthquakes by year
2. Earthquakes by month
3. Magnitude distribution
4. Depth distribution
5. Top countries by earthquake count
6. Magnitude versus depth
7. Earthquakes by day of week
8. Earthquakes by depth category
9. Earthquakes by magnitude category
10. Top strongest earthquakes

Visualization script:

```text
04_visualization.py
```

## Streamlit Dashboard

An interactive Streamlit dashboard was created to present the earthquake analysis.

The dashboard displays:

- Total number of earthquakes
- Strongest earthquake magnitude
- Deepest earthquake
- Number of tsunami events
- Earthquakes by year
- Earthquakes by month
- Magnitude distribution
- Depth distribution
- Top 10 countries
- Magnitude versus depth
- Global earthquake locations
- Top 10 strongest earthquakes

Streamlit application:

```text
05_app.py
```

## Key Results

The analysis identified the following overall results from the dataset:

- Total earthquake records: 104,442
- Strongest recorded magnitude: 8.8
- Deepest recorded earthquake: 681.24 km
- Tsunami-associated events: 625

These results are based on the collected USGS earthquake dataset for 2021–2025.

## Project Structure

```text
Global_Seismic_Trends/
│
├── data/
│   └── cleaned_earthquake_data_2021_2025.csv
│
├── sql/
│   └── earthquake_analysis.sql
│
├── 01_retrieve_data.py
├── 02_data_cleaning.py
├── 03_mysql_upload.py
├── 04_visualization.py
├── 05_app.py
└── README.md
```

## How to Run the Project

### Step 1: Open the project folder

```text
E:\OneDrive\Desktop\Global_Seismic_Trends
```

### Step 2: Activate the virtual environment

```powershell
.venv\Scripts\Activate.ps1
```

### Step 3: Install required libraries

```powershell
pip install requests pandas sqlalchemy pymysql matplotlib seaborn streamlit
```

### Step 4: Retrieve earthquake data

```powershell
python 01_retrieve_data.py
```

### Step 5: Clean the data

```powershell
python 02_data_cleaning.py
```

### Step 6: Upload data to MySQL

```powershell
python 03_mysql_upload.py
```

### Step 7: Run Python visualizations

```powershell
python 04_visualization.py
```

### Step 8: Run Streamlit dashboard

```powershell
streamlit run 05_app.py
```

The Streamlit dashboard will open in the browser.

## Conclusion

This project demonstrates a complete data science workflow starting from real-world API data collection and ending with an interactive dashboard.

The project combines Python, Pandas, data cleaning, feature engineering, MySQL, SQL analysis, data visualization, and Streamlit to study global earthquake activity.

## Author

Kabilnath SJ

## Project Title

Global Seismic Trends: Data-Driven Earthquake Insights

## Data Source

USGS Earthquake Hazards Program
