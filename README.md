# World Development Indicators  Python ETL Pipeline

# Project Overview

This project builds a production-style ETL pipeline using the World Bank World Development Indicators (WDI) dataset.

The pipeline extracts raw global development data, transforms it into a structured format, and loads it into a PostgreSQL database for analysis and visualization.



# Objectives

Convert raw wide-format data into analysis-ready long format
Ensure data quality through validation checks
Implement safe and reliable data loading using transactions
Design a scalable ETL structure using modular Python scripts


# Project Structure
```
wdi_etl_project/
│

├── extract.py                      # Extract raw CSV data

├── transform.py                    # Clean and reshape data

├── load.py                         # Load data into PostgreSQL

├── main.py                         # Pipeline orchestrator

├── postgresSQL_verification.sql    # Verify ETL in database

├── dashboard.pbix                  # Log file (optional)

└── WDIData.csv                     # Raw dataset
```


# ETL Pipeline Flow

- Extraction

Reads the raw CSV file (WDIData.csv)
Outputs a raw DataFrame (raw_df)

- Transformation

Converts wide data (years as columns) into long format
Removes missing values
Enforces correct data types
Outputs cleaned DataFrame (clean_df)

- Load

Connects to PostgreSQL using SQLAlchemy
Loads data into a table (fact_wdi)
Uses transaction control to prevent partial loads


## Key Concepts Implemented

ETL pipeline design
Data reshaping (wide → long)
Data validation (null checks, row counts)
Error handling with try/except
Transaction-safe database loading
Modular Python architecture


## Dataset

Source: World Bank – World Development Indicators (WDI)

Global dataset covering 200+ countries
Time series data from 1960–2024
Includes indicators such as GDP, population, and life expectancy


## Technologies Used

Python
pandas
SQLAlchemy
PostgreSQL


## How to Run the Pipeline

```
Install dependencies:
pip install pandas sqlalchemy psycopg2-binary

Update database connection in main.py:
postgresql://username:password@localhost:5432/etl_db

Run the pipeline:
python main.py
```



## Data Validation

The pipeline includes:

Row count validation
Null value checks
Post-load validation against database


## Error Handling

Extraction errors (missing file, read issues)
Transformation validation errors
Database connection failures
Transaction rollback on failure


# Data Visualization

To derive insights from the transformed dataset, several visual analyses were performed:

- Global Trends

Line charts showing long-term trends in key indicators such as:
Life expectancy
GDP growth
Population

- Country Comparisons

Multi-country comparisons (e.g., Nigeria, USA, China, India)
Highlights development gaps and growth differences

- Top & Bottom Analysis

Bar charts identifying:
Top countries by GDP
Countries with lowest life expectancy

- Regional Insights

Aggregated analysis by region to compare development patterns


## Key Insights

Global life expectancy has steadily increased over time
Significant disparities exist between developed and developing countries
Higher GDP generally correlates with higher life expectancy
Rapid population growth is concentrated in specific regions


## Tools Used for Visualization

Power BI


# Summary

This project demonstrates the transition from notebook-based analysis to a structured, production-ready ETL pipeline, incorporating best practices in data engineering such as modular design, validation, and safe data loading.