# Q7. Create a program that stores employee records in tuples. 
# Each tuple should contain employee ID, name, and salary. 
# Display employees whose salary is above the average salary.

def above_avg_salary(emps):
    avg = sum(e[2] for e in emps) / len(emps)
    print(f"Avg Salary: ${avg:.2f}")
    for e in emps:
        if e[2] > avg:
            print(f"ID: {e[0]}, Name: {e[1]}, Salary: ${e[2]}")

if __name__ == "__main__":
    records = [(1, "Alice", 75000), (2, "Bob", 50000), (3, "Charlie", 90000)]
    above_avg_salary(records)

# Expected Output:
# Avg Salary: $71666.67
# ID: 1, Name: Alice, Salary: $75000
# ID: 3, Name: Charlie, Salary: $90000
