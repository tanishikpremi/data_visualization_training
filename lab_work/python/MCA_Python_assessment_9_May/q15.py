# Q15. Write a Pandas program to read employee data from a CSV file 
# and display department-wise average salary and highest salary employee.

import pandas as pd

def process_employee_data():
    data = "EmpID,Name,Dept,Salary\n1,John,IT,70000\n2,Jane,HR,60000\n3,Doe,IT,80000\n4,Smith,Finance,75000"
    with open('employee_data.csv', 'w') as f:
        f.write(data)
        
    df = pd.read_csv('employee_data.csv')
    
    print("Dept-wise Avg Salary:")
    print(df.groupby('Dept')['Salary'].mean())
    
    print("\nHighest Salary Employee:")
    highest = df.loc[df['Salary'].idxmax()]
    print(highest[['Name', 'Salary']].to_string())

if __name__ == "__main__":
    process_employee_data()

# Expected Output:
# Dept-wise Avg Salary:
# Dept
# Finance    75000.0
# HR         60000.0
# IT         75000.0
# Name: Salary, dtype: float64
# 
# Highest Salary Employee:
# Name        Doe
# Salary    80000
