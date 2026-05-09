# Q29. Create a DataFrame containing student marks in multiple subjects. 
# Calculate total marks, percentage, and assign grades using apply() function.

import pandas as pd

def assign_grade(pct):
    if pct >= 90: return 'A'
    elif pct >= 80: return 'B'
    elif pct >= 70: return 'C'
    else: return 'F'

def process_student_df():
    df = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Math': [95, 70, 85],
        'Science': [90, 65, 80]
    })
    
    df['Total'] = df['Math'] + df['Science']
    df['Percentage'] = df['Total'] / 2
    df['Grade'] = df['Percentage'].apply(assign_grade)
    
    print(df)

if __name__ == "__main__":
    process_student_df()

# Expected Output:
#       Name  Math  Science  Total  Percentage Grade
# 0    Alice    95       90    185        92.5     A
# 1      Bob    70       65    135        67.5     F
# 2  Charlie    85       80    165        82.5     B
