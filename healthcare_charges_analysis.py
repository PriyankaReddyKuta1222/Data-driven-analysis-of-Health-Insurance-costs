import pymssql
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # Database Connection
    try:
        # Replace these values with your SQL Server details
        server = 'localhost'  # Replace with your server name
        user = 'your_username'  # Replace with your username
        password = 'your_password'  # Replace with your password
        database = 'Healthcare_Insurance'  # Replace with your database name

        # Establish connection
        conn = pymssql.connect(server=server, user=user, password=password, database=database)
        print("Connected to SQL Server database")

        # Fetch Data
        query = "SELECT age, sex, bmi, smoker, region, charges FROM Patients;"
        df = pd.read_sql(query, conn)

        # Data Visualization

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

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if conn:
            conn.close()
            print("SQL Server connection closed")

if __name__ == "__main__":
    main()
