"""
CLASS WORK | Pandas - Basics
Topic: Series, DataFrame Creation, Reading Data, Basic Info
"""

import pandas as pd
import numpy as np

# ─────────────────────────────────────────────
# QUESTIONS
# ─────────────────────────────────────────────

# Q1. Create a Pandas Series from a list of temperatures.
temps = pd.Series([22.5, 30.1, 28.3, 25.0, 18.7])
print("Q1:\n", temps)

# Q2. Create a DataFrame from a dictionary of employee data.
data = {
    "Name":       ["Alice", "Bob", "Charlie", "Diana"],
    "Department": ["HR",    "IT",  "Finance",  "IT"],
    "Salary":     [55000,   72000, 61000,      68000],
    "Experience": [3,       5,     4,          6]
}
df = pd.DataFrame(data)
print("\nQ2:\n", df)

# Q3. Display basic info and statistics.
print("\nQ3 Info:")
df.info()
print("\nQ3 Describe:\n", df.describe())

# Q4. Select a single column and multiple columns.
print("\nQ4 Names:\n", df["Name"])
print("\nQ4 Name & Salary:\n", df[["Name", "Salary"]])

# Q5. Filter employees in the IT department.
it_dept = df[df["Department"] == "IT"]
print("\nQ5 IT Department:\n", it_dept)

# Q6. Filter employees with Salary > 60000 and Experience >= 5.
senior = df[(df["Salary"] > 60000) & (df["Experience"] >= 5)]
print("\nQ6 Senior High Earners:\n", senior)

# Q7. Add a new column "Annual Bonus" (10% of salary).
df["Annual Bonus"] = df["Salary"] * 0.10
print("\nQ7:\n", df)

# Q8. Sort the DataFrame by Salary in descending order.
print("\nQ8:\n", df.sort_values("Salary", ascending=False))

# Q9. Group by Department and get mean salary.
print("\nQ9:\n", df.groupby("Department")["Salary"].mean())

# Q10. Check for missing values and fill with mean.
df_with_nan = df.copy()
df_with_nan.loc[1, "Salary"] = np.nan
print("\nQ10 Null Count:\n", df_with_nan.isnull().sum())
df_with_nan["Salary"].fillna(df_with_nan["Salary"].mean(), inplace=True)
print("Q10 After Fill:\n", df_with_nan)
