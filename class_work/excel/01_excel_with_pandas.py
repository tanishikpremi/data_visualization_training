"""
CLASS WORK | Excel - Working with Excel in Python (openpyxl / pandas)
Topic: Reading, Writing, Formatting Excel Files
"""

import pandas as pd

# ─────────────────────────────────────────────
# QUESTIONS
# ─────────────────────────────────────────────

# Q1. Create a DataFrame and write it to an Excel file.
sales_data = {
    "Month":    ["Jan","Feb","Mar","Apr","May","Jun"],
    "Sales":    [15000, 18200, 21500, 17300, 22000, 25600],
    "Expenses": [9000,  10500, 11000, 9800,  12000, 13000],
    "Profit":   [6000,  7700,  10500, 7500,  10000, 12600]
}
df = pd.DataFrame(sales_data)
df.to_excel("sales_report.xlsx", index=False, sheet_name="Monthly Sales")
print("Q1: Excel file created → sales_report.xlsx")

# Q2. Read back the Excel file.
df_read = pd.read_excel("sales_report.xlsx", sheet_name="Monthly Sales")
print("\nQ2 Read Excel:\n", df_read)

# Q3. Write multiple sheets to one Excel file.
students = pd.DataFrame({
    "Name": ["Alice","Bob","Charlie"],
    "Grade": ["A","B","A"]
})
courses = pd.DataFrame({
    "Course": ["Python","SQL","Excel"],
    "Credits": [3, 3, 2]
})
with pd.ExcelWriter("school_data.xlsx") as writer:
    students.to_excel(writer, sheet_name="Students", index=False)
    courses.to_excel(writer, sheet_name="Courses", index=False)
print("\nQ3: Multi-sheet Excel created → school_data.xlsx")

# Q4. Read a specific sheet and specific columns.
df_students = pd.read_excel("school_data.xlsx", sheet_name="Students", usecols=["Name"])
print("\nQ4 Students (Name only):\n", df_students)

# Q5. Add a calculated column and re-export.
df["Profit Margin %"] = (df["Profit"] / df["Sales"] * 100).round(2)
df.to_excel("sales_with_margin.xlsx", index=False)
print("\nQ5 Updated Excel with Profit Margin saved.")

# Q6. Get summary statistics and save to Excel.
summary = df.describe().round(2)
summary.to_excel("summary_stats.xlsx")
print("\nQ6 Summary stats saved to summary_stats.xlsx")
