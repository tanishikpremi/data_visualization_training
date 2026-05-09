# Q39. Read a CSV file containing student attendance records and 
# display students with attendance below 75%.

import pandas as pd

def check_attendance():
    data = "Name,TotalClasses,Attended\nAlice,40,35\nBob,40,25\nCharlie,40,38\nDavid,40,20"
    with open('attendance.csv', 'w') as f: f.write(data)
    
    df = pd.read_csv('attendance.csv')
    df['Percentage'] = (df['Attended'] / df['TotalClasses']) * 100
    
    low_attendance = df[df['Percentage'] < 75]
    print("Students with < 75% attendance:")
    print(low_attendance[['Name', 'Percentage']].to_string(index=False))

if __name__ == "__main__":
    check_attendance()

# Expected Output:
# Students with < 75% attendance:
#  Name  Percentage
#   Bob        62.5
# David        50.0
