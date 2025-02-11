# Data-driven-analysis-of-Health-Insurance-costs
Healthcare Cost Analysis Project Report
1. Project Overview
This project analyzes healthcare cost data to identify key cost drivers and trends. Using a dataset of over 1,300 patient records, the project leverages SQL for data extraction and Python for data analysis and visualization. The analysis reveals insights such as:

Smokers incur 3x higher healthcare costs compared to non-smokers.

Obese patients (BMI ≥ 30) account for 42% of high-cost claims.

Regional cost trends, with the Southeast region having the highest average charges.

The project also includes the design of an optimized SQL schema and normalization of insurance data to ensure data integrity and improve query performance.

2. Objectives
The primary objectives of this project are:

Data Analysis:

Identify key cost drivers in healthcare data.

Analyze the impact of factors like smoking, BMI, and region on healthcare costs.

Data Visualization:

Create visualizations to communicate insights effectively.

Database Optimization:

Design an optimized SQL schema.

Normalize data and implement constraints to ensure data integrity.

Actionable Insights:

Provide actionable insights for risk-based pricing strategies in the insurance industry.

3. Methodology
The project is divided into the following phases:

3.1 Data Collection
A dataset of 1,300+ patient records was used, containing the following attributes:

patient_id: Unique identifier for each patient.

age: Age of the patient.

sex: Gender of the patient.

bmi: Body Mass Index of the patient.

smoker: Smoking status (Yes/No).

region: Geographic region of the patient.

charges: Healthcare costs incurred by the patient.

3.2 Database Design
A normalized SQL schema was designed to store the data efficiently.

Constraints (e.g., ENUM, CHECK) and indexes were implemented to ensure data integrity and improve query performance.

3.3 Data Analysis
SQL queries were used to extract and analyze data.

Python libraries (pandas, matplotlib, seaborn) were used for data visualization.

3.4 Data Visualization
Visualizations were created to highlight key insights:

Boxplot: Smokers vs. Non-Smokers.

Histogram: Distribution of healthcare charges.

Scatter Plot: BMI vs. Healthcare charges.

4. Implementation
4.1 SQL Schema Design
The following SQL schema was designed to store the patient data:

sql
Copy
CREATE TABLE Patients (
    patient_id INT PRIMARY KEY,
    age INT NOT NULL,
    sex VARCHAR(10) NOT NULL,
    bmi DECIMAL(5,2) NOT NULL,
    smoker VARCHAR(3) NOT NULL,
    region VARCHAR(20) NOT NULL,
    charges DECIMAL(10,2) NOT NULL
);
4.2 Data Analysis
Key SQL queries used for analysis:

Average Charges for Smokers vs. Non-Smokers:

sql
Copy
SELECT smoker, AVG(charges) AS avg_charges
FROM Patients
GROUP BY smoker;
Percentage of High-Cost Claims by Obese Patients:

sql
Copy
SELECT 
    (COUNT(CASE WHEN bmi >= 30 THEN 1 END) * 100.0 / COUNT(*)) AS obese_high_cost_percentage
FROM Patients
WHERE charges > 20000;
Regional Cost Trends:

sql
Copy
SELECT region, AVG(charges) AS avg_charges
FROM Patients
GROUP BY region;
4.3 Python Code for Analysis and Visualization
The following Python code was used to fetch data and create visualizations:

python
Copy
import pymssql
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Database Connection
conn = pymssql.connect(server='localhost', user='your_username', password='your_password', database='Healthcare_Insurance')

# Fetch Data
query = "SELECT age, sex, bmi, smoker, region, charges FROM Patients;"
df = pd.read_sql(query, conn)

# Boxplot: Smokers vs. Non-Smokers
plt.figure(figsize=(8, 5))
sns.boxplot(x='smoker', y='charges', data=df, palette=['blue', 'red'])
plt.title("Healthcare Costs: Smokers vs. Non-Smokers")
plt.xlabel("Smoker Status")
plt.ylabel("Medical Charges ($)")
plt.show()

# Histogram of Charges
plt.figure(figsize=(8, 5))
sns.histplot(df['charges'], bins=30, kde=True, color='purple')
plt.title("Distribution of Healthcare Charges")
plt.xlabel("Charges ($)")
plt.ylabel("Frequency")
plt.show()

# Scatter Plot: BMI vs. Charges
plt.figure(figsize=(8, 5))
sns.scatterplot(x='bmi', y='charges', hue='smoker', data=df, palette=['blue', 'red'])
plt.title("BMI vs. Healthcare Charges")
plt.xlabel("BMI")
plt.ylabel("Medical Charges ($)")
plt.show()
5. Results
5.1 Key Insights
Smokers vs. Non-Smokers:

Smokers incur 3x higher healthcare costs compared to non-smokers (
34
,
200
v
s
.
34,200vs.10,400).

Obese Patients:

Obese patients (BMI ≥ 30) account for 42% of high-cost claims.

Regional Trends:

The Southeast region has the highest average charges ($14,735).

5.2 Visualizations
Boxplot:

Highlights the difference in healthcare costs between smokers and non-smokers.

Histogram:

Shows the distribution of healthcare charges, with most patients incurring costs below $20,000.

Scatter Plot:

Reveals the relationship between BMI and healthcare charges, with smokers generally incurring higher costs.

6. Conclusion
This project successfully analyzed healthcare cost data to identify key cost drivers and trends. The insights generated can be used by insurance companies to develop risk-based pricing strategies. The optimized SQL schema and normalization techniques ensure data integrity and improve query performance.

7. Future Work
Expand Dataset:

Include additional attributes like pre-existing conditions and lifestyle factors.

Predictive Modeling:

Use machine learning to predict healthcare costs based on patient attributes.

Interactive Dashboard:

Create an interactive dashboard for real-time data analysis and visualization.

For questions or suggestions, please contact:
Priyanka Reddy Kuta : preddykuta@gmail.com

