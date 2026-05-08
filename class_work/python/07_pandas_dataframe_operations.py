"""
CLASS WORK | Pandas - DataFrame Operations
Topic: Merging, Pivot Tables, Apply, String Methods, DateTime
"""

import pandas as pd
import numpy as np

# ─────────────────────────────────────────────
# QUESTIONS
# ─────────────────────────────────────────────

# Q1. Merge two DataFrames on a common key.
orders = pd.DataFrame({"OrderID": [1,2,3,4], "CustomerID": [101,102,101,103], "Amount": [250,480,130,560]})
customers = pd.DataFrame({"CustomerID": [101,102,103], "Name": ["Alice","Bob","Charlie"]})
merged = pd.merge(orders, customers, on="CustomerID")
print("Q1 Merged:\n", merged)

# Q2. Create a pivot table showing total Amount per Customer.
pivot = merged.pivot_table(values="Amount", index="Name", aggfunc="sum")
print("\nQ2 Pivot:\n", pivot)

# Q3. Use apply() to create a new column with a custom function.
df = pd.DataFrame({"Score": [45, 82, 60, 91, 55, 73]})
def grade(s):
    if s >= 80: return "A"
    elif s >= 60: return "B"
    else: return "C"
df["Grade"] = df["Score"].apply(grade)
print("\nQ3:\n", df)

# Q4. Use string methods on a column.
names = pd.Series(["  alice  ", "BOB", "Charlie", "diana"])
print("\nQ4 Strip & Title:", names.str.strip().str.title().tolist())
print("Q4 Upper:", names.str.upper().tolist())

# Q5. Work with datetime columns.
df_time = pd.DataFrame({"Date": pd.to_datetime(["2024-01-15","2024-03-22","2024-07-04","2024-12-31"])})
df_time["Month"] = df_time["Date"].dt.month_name()
df_time["DayOfWeek"] = df_time["Date"].dt.day_name()
df_time["Quarter"] = df_time["Date"].dt.quarter
print("\nQ5:\n", df_time)

# Q6. Use value_counts() on a categorical column.
departments = pd.Series(["IT","HR","IT","Finance","IT","HR","Finance","IT"])
print("\nQ6:\n", departments.value_counts())

# Q7. Drop duplicate rows.
df_dup = pd.DataFrame({"A": [1,2,2,3,1], "B": ["x","y","y","z","x"]})
print("\nQ7 Before:", len(df_dup), "rows")
df_dup = df_dup.drop_duplicates()
print("Q7 After:", len(df_dup), "rows")

# Q8. Rename columns.
df_r = pd.DataFrame({"fn": ["Alice","Bob"], "ln": ["Smith","Jones"], "ag": [25, 30]})
df_r.rename(columns={"fn":"FirstName","ln":"LastName","ag":"Age"}, inplace=True)
print("\nQ8:\n", df_r)

# Q9. Use loc and iloc to access rows/columns.
df_main = pd.DataFrame({"X": range(1,6), "Y": range(10,60,10), "Z": range(100,600,100)})
print("\nQ9 loc row 2:", df_main.loc[2])
print("Q9 iloc [0:2, 0:2]:\n", df_main.iloc[0:2, 0:2])

# Q10. Compute correlation matrix.
df_corr = pd.DataFrame(np.random.rand(5, 3), columns=["A","B","C"])
print("\nQ10 Correlation:\n", df_corr.corr().round(2))
