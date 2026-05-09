# Q2. Develop a grading system where marks of five subjects are entered by the user. 
# The program should calculate percentage, assign grades using nested if-else conditions, 
# and identify whether the student qualifies for a scholarship.

def grading_system(marks):
    total = sum(marks)
    percentage = (total / 500) * 100
    grade = ""
    scholarship = False
    
    if percentage >= 90:
        grade = "A+"
        if percentage >= 95: scholarship = True
    elif percentage >= 80: grade = "A"
    elif percentage >= 70: grade = "B"
    elif percentage >= 60: grade = "C"
    elif percentage >= 50: grade = "D"
    else: grade = "F"
        
    print(f"Total Marks: {total}/500")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")
    print(f"Scholarship: {'Yes' if scholarship else 'No'}")

if __name__ == "__main__":
    grading_system([95, 96, 92, 98, 94])

# Expected Output:
# Total Marks: 475/500
# Percentage: 95.00%
# Grade: A+
# Scholarship: Yes
