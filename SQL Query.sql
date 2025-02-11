USE Healthcare_Insurance;
GO

-- Drop the table if it already exists
IF OBJECT_ID('Patients', 'U') IS NOT NULL
    DROP TABLE Patients;

-- Create the Patients table
CREATE TABLE Patients (
    patient_id INT PRIMARY KEY,
    age INT NOT NULL,
    sex VARCHAR(10) NOT NULL,
    bmi DECIMAL(5,2) NOT NULL,
    smoker VARCHAR(3) NOT NULL,
    region VARCHAR(20) NOT NULL,
    charges DECIMAL(10,2) NOT NULL
);