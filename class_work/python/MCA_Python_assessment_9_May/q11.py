# Q11. Create a text file containing student marks. Read the file and display 
# the topper, average marks, and students scoring below average.

def process_marks(filename):
    with open(filename, 'w') as f:
        f.write("Alice,85\nBob,92\nCharlie,78\nDavid,95\nEve,60\n")
        
    students = {}
    with open(filename, 'r') as f:
        for line in f:
            name, mark = line.strip().split(',')
            students[name] = int(mark)
            
    avg = sum(students.values()) / len(students)
    topper = max(students, key=students.get)
    below_avg = [name for name, mark in students.items() if mark < avg]
    
    print(f"Topper: {topper} ({students[topper]})")
    print(f"Average Marks: {avg}")
    print(f"Below Average: {', '.join(below_avg)}")

if __name__ == "__main__":
    process_marks("student_marks.txt")

# Expected Output:
# Topper: David (95)
# Average Marks: 82.0
# Below Average: Charlie, Eve
