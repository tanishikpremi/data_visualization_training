rating = int(input("Enter performance rating (1-5): "))
experience = float(input("Enter years of experience: "))
attendance = float(input("Enter attendance percentage: "))

increment = 0

if rating == 5:
    increment += 15
elif rating == 4:
    increment += 10
elif rating == 3:
    increment += 5

if experience >= 5:
    increment += 5

if attendance >= 95:
    increment += 2

print(f"Calculated Salary Increment: {increment}%")