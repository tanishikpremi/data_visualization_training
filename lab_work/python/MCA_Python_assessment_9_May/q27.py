# Q27. Create tuples containing student names and courses. 
# Convert them into sets to identify students enrolled in multiple courses.

def identify_multi_course_students(student_course_tuples):
    course_records = {}
    for student, course in student_course_tuples:
        if student not in course_records:
            course_records[student] = set()
        course_records[student].add(course)
        
    print("Students in multiple courses:")
    for student, courses in course_records.items():
        if len(courses) > 1:
            print(f"{student}: {courses}")

if __name__ == "__main__":
    records = [("Alice", "Math"), ("Bob", "Science"), ("Alice", "Art"), ("Charlie", "Math")]
    identify_multi_course_students(records)

# Expected Output:
# Students in multiple courses:
# Alice: {'Art', 'Math'}
