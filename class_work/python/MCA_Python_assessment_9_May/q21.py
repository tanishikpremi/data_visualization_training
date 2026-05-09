# Q21. Generate a NumPy array of student marks and convert it into a Pandas DataFrame. 
# Display highest marks, average marks, and subject-wise statistics.

import numpy as np
import pandas as pd

def process_marks():
    marks_array = np.array([[85, 90, 88], [78, 85, 80], [92, 95, 89]])
    df = pd.DataFrame(marks_array, columns=['Math', 'Science', 'English'], index=['Alice', 'Bob', 'Charlie'])
    
    print("DataFrame:\n", df)
    print("\nHighest Marks:\n", df.max())
    print("\nAverage Marks:\n", df.mean())
    print("\nSubject-wise Stats:\n", df.describe().loc[['mean', 'max', 'min']])

if __name__ == "__main__":
    process_marks()

# Expected Output:
# DataFrame:
#           Math  Science  English
# Alice      85       90       88
# Bob        78       85       80
# Charlie    92       95       89
# Highest Marks:
# Math       92
# Science    95
# English    89
# Average Marks:
# Math       85.0
# Science    90.0
# English    85.666667
# Subject-wise Stats:
#       Math  Science    English
# mean  85.0     90.0  85.666667
# max   92.0     95.0  89.000000
# min   78.0     85.0  80.000000
