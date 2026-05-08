"""
self learning - excel vlookup/xlookup equivalent in pandas
i was reading about VLOOKUP and tried to replicate it in python
turns out pandas merge() does the same thing and is more powerful
"""

import pandas as pd

# ── setup: two tables like you'd have in Excel ────

employees = pd.DataFrame({
    "emp_id":     [101, 102, 103, 104, 105],
    "name":       ["Alice", "Bob", "Charlie", "Diana", "Ethan"],
    "dept_id":    [10, 20, 10, 30, 20]
})

departments = pd.DataFrame({
    "dept_id":   [10, 20, 30, 40],
    "dept_name": ["HR", "IT", "Finance", "Marketing"],
    "location":  ["Mumbai", "Bangalore", "Delhi", "Pune"]
})

# ── VLOOKUP equivalent = merge ─────────────────

result = pd.merge(employees, departments, on="dept_id", how="left")
print("VLOOKUP equivalent (merge):\n", result)

# ── INDEX-MATCH equivalent ─────────────────────
# in excel: =INDEX(dept_name_col, MATCH(emp_dept_id, dept_id_col, 0))

dept_map = departments.set_index("dept_id")["dept_name"]
employees["dept_name"] = employees["dept_id"].map(dept_map)
print("\nINDEX-MATCH equivalent (map):\n", employees)

# ── XLOOKUP with default fallback ─────────────
# if dept_id not found, use "Unknown"

employees2 = pd.DataFrame({
    "emp_id":  [106, 107],
    "name":    ["Frank", "Grace"],
    "dept_id": [99, 10]   # 99 doesn't exist
})

employees2["dept_name"] = employees2["dept_id"].map(dept_map).fillna("Unknown")
print("\nXLOOKUP with fallback:\n", employees2)

# ── HLOOKUP equivalent - looking up across columns ──
# less common, but pivot/transpose can help

# ── SUMIF equivalent in pandas ─────────────────
# =SUMIF(dept_col, "IT", salary_col)

salaries = pd.DataFrame({
    "name":   ["Alice","Bob","Charlie","Diana","Ethan"],
    "dept":   ["HR","IT","IT","Finance","HR"],
    "salary": [55000, 72000, 68000, 61000, 58000]
})

it_total = salaries[salaries["dept"] == "IT"]["salary"].sum()
print(f"\nSUMIF - Total IT salary: ₹{it_total:,}")

# ── COUNTIF equivalent ─────────────────────────
it_count = (salaries["dept"] == "IT").sum()
print(f"COUNTIF - IT employees: {it_count}")

# ── AVERAGEIFS equivalent ──────────────────────
# avg salary for IT dept where salary > 65000
filtered = salaries[(salaries["dept"] == "IT") & (salaries["salary"] > 65000)]
print(f"AVERAGEIFS: ₹{filtered['salary'].mean():,.0f}")
