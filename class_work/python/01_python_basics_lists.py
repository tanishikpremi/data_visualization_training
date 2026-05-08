"""
CLASS WORK | Python Basics - Lists
Topic: List Creation, Indexing, Slicing, Methods
"""

# ─────────────────────────────────────────────
# QUESTIONS
# ─────────────────────────────────────────────

# Q1. Create a list of 5 fruits and print the third element.
fruits = ["apple", "banana", "cherry", "mango", "orange"]
print("Q1:", fruits[2])

# Q2. Append "grape" to the list and print the updated list.
fruits.append("grape")
print("Q2:", fruits)

# Q3. Remove "banana" from the list.
fruits.remove("banana")
print("Q3:", fruits)

# Q4. Slice the first 3 elements from the list.
print("Q4:", fruits[:3])

# Q5. Reverse the list without using reverse().
print("Q5:", fruits[::-1])

# Q6. Sort a list of numbers in ascending and descending order.
numbers = [34, 2, 89, 12, 56, 7]
print("Q6 Asc:", sorted(numbers))
print("Q6 Desc:", sorted(numbers, reverse=True))

# Q7. Find the length, min, and max of the numbers list.
print("Q7 Length:", len(numbers), "| Min:", min(numbers), "| Max:", max(numbers))

# Q8. Create a list of squares of numbers from 1 to 10 using list comprehension.
squares = [x**2 for x in range(1, 11)]
print("Q8:", squares)

# Q9. Count how many times 5 appears in this list.
data = [5, 3, 5, 7, 5, 9, 2, 5]
print("Q9:", data.count(5))

# Q10. Flatten this nested list: [[1,2], [3,4], [5,6]]
nested = [[1, 2], [3, 4], [5, 6]]
flat = [item for sublist in nested for item in sublist]
print("Q10:", flat)
