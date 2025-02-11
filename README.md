# Data-driven-analysis-of-Health-Insurance-costs

Overview

This project analyzes healthcare insurance costs using a synthetic dataset of 1,300+ patient records. The objective is to identify key factors influencing medical expenses, such as smoking, obesity (BMI ≥ 30), and age. SQL queries and Python-based data visualizations provide insights into the cost distribution and trends.

Key Findings

Smokers incur 3x higher medical charges than non-smokers.

Obese patients (BMI ≥ 30) contribute to 42% of high-cost claims.

Query optimization reduced runtime by 30%.

Technologies Used

Database: MySQL

Query Optimization: Indexing, WHERE filters, Aggregations

Data Analysis & Visualization: Python (Pandas, Matplotlib, Seaborn)

Version Control: Git & GitHub

Dataset

The dataset includes the following fields:

patient_id - Unique identifier

age - Patient age (18-80)

sex - Male/Female

bmi - Body Mass Index (18-45)

smoker - Yes/No

region - Northeast, Northwest, Southeast, Southwest

charges - Healthcare insurance cost (USD)

Download Dataset: healthcare_insurance_costs.csv

Setup & Usage

1. Clone the Repository

git clone https://github.com/yourusername/healthcare-insurance-analysis.git
cd healthcare-insurance-analysis

2. Install Dependencies

pip install pandas matplotlib mysql-connector-python seaborn

3. Import Dataset into MySQL

CREATE DATABASE Healthcare_Insurance;
USE Healthcare_Insurance;

CREATE TABLE Patients (
    patient_id INT PRIMARY KEY,
    age INT,
    sex ENUM('Male', 'Female'),
    bmi DECIMAL(5,2),
    smoker ENUM('Yes', 'No'),
    region ENUM('Northeast', 'Northwest', 'Southeast', 'Southwest'),
    charges DECIMAL(10,2)
);

LOAD DATA INFILE 'healthcare_insurance_costs.csv'
INTO TABLE Patients
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

4. Run Analysis Script

python analysis.py

Sample Visualization

Example: Smoker vs. Non-Smoker Medical Costs

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("healthcare_insurance_costs.csv")

plt.figure(figsize=(8, 5))
sns.boxplot(x='smoker', y='charges', data=df, palette=['blue', 'red'])
plt.title("Healthcare Costs: Smokers vs. Non-Smokers")
plt.show()

Future Enhancements

Integrate Machine Learning to predict healthcare costs.

Develop an interactive dashboard for real-time insights.

Scale the database for larger datasets using cloud solutions.
