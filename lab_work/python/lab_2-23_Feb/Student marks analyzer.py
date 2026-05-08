def analyze_marks(marks):

    valid_marks = [m for m in marks if 0 <= m <= 100]
    
    if not valid_marks:
        return "No valid marks available."
        
 
    average = sum(valid_marks) / len(valid_marks)
    
 
    highest_mark = max(valid_marks)
    toppers = [m for m in valid_marks if m == highest_mark]
  
    if average >= 90: grade = 'A'
    elif average >= 75: grade = 'B'
    elif average >= 50: grade = 'C'
    else: grade = 'D'
    
    print(f"Valid Marks: {valid_marks}")
    print(f"Average: {average:.2f}")
    print(f"Topper Score: {highest_mark}")
    print(f"Class Grade: {grade}")


analyze_marks([45, 105, 88, -5, 92, 92, 76])