"""
CLASS WORK | Python Basics - Tuples
Topic: Tuple Creation, Immutability, Packing/Unpacking, Methods
"""

# ─────────────────────────────────────────────
# QUESTIONS
# ─────────────────────────────────────────────

# Q1. Create a tuple with 5 city names and print the second city.
cities = ("New York", "London", "Tokyo", "Paris", "Dubai")
print("Q1:", cities[1])

# Q2. Try to change the first element — explain why it fails.
# cities[0] = "Berlin"  # ❌ TypeError: 'tuple' object does not support item assignment
print("Q2: Tuples are immutable — elements cannot be changed after creation.")

# Q3. Unpack a tuple into individual variables.
coordinates = (28.61, 77.20)
lat, lon = coordinates
print(f"Q3: Latitude = {lat}, Longitude = {lon}")

# Q4. Find the index of "Tokyo" in the cities tuple.
print("Q4 Index:", cities.index("Tokyo"))

# Q5. Count how many times 7 appears in this tuple.
nums = (7, 3, 7, 9, 7, 1, 4)
print("Q5:", nums.count(7))

# Q6. Convert a tuple to a list, add an element, and convert back.
t = (1, 2, 3)
lst = list(t)
lst.append(4)
t = tuple(lst)
print("Q6:", t)

# Q7. Merge two tuples.
t1 = (1, 2, 3)
t2 = (4, 5, 6)
print("Q7:", t1 + t2)

# Q8. Slice the last 3 elements of a tuple.
data = (10, 20, 30, 40, 50, 60)
print("Q8:", data[-3:])

# Q9. Check if "Paris" exists in the cities tuple.
print("Q9:", "Paris" in cities)

# Q10. Create a tuple of tuples representing a 2x2 matrix and access element at row 1, col 1.
matrix = ((1, 2), (3, 4))
print("Q10:", matrix[1][1])
