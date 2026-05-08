"""
CLASS WORK | Python Basics - Dictionaries
Topic: Dict Creation, CRUD, Looping, Nesting, Comprehension
"""

# ─────────────────────────────────────────────
# QUESTIONS
# ─────────────────────────────────────────────

# Q1. Create a dictionary for a student with name, age, and grade.
student = {"name": "Alice", "age": 21, "grade": "A"}
print("Q1:", student)

# Q2. Access the student's name and age.
print("Q2 Name:", student["name"], "| Age:", student["age"])

# Q3. Add a new key "city" with value "Mumbai".
student["city"] = "Mumbai"
print("Q3:", student)

# Q4. Update the grade to "A+".
student["grade"] = "A+"
print("Q4:", student)

# Q5. Delete the "city" key.
del student["city"]
print("Q5:", student)

# Q6. Loop through all keys and values.
print("Q6:")
for key, value in student.items():
    print(f"  {key}: {value}")

# Q7. Check if "age" key exists in the dictionary.
print("Q7:", "age" in student)

# Q8. Get all keys, values, and items.
print("Q8 Keys:", list(student.keys()))
print("Q8 Values:", list(student.values()))

# Q9. Create a dict from two lists using zip().
keys = ["a", "b", "c"]
values = [1, 2, 3]
combined = dict(zip(keys, values))
print("Q9:", combined)

# Q10. Use dict comprehension to create {1:1, 2:4, 3:9, 4:16, 5:25}
squares = {x: x**2 for x in range(1, 6)}
print("Q10:", squares)

# Q11. Nested dictionary — access the score of subject "Math".
student_records = {
    "name": "Bob",
    "scores": {"Math": 95, "Science": 88, "English": 76}
}
print("Q11 Math Score:", student_records["scores"]["Math"])

# Q12. Merge two dictionaries (Python 3.9+).
d1 = {"x": 1, "y": 2}
d2 = {"y": 99, "z": 3}
merged = {**d1, **d2}
print("Q12:", merged)
