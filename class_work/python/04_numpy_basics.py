"""
CLASS WORK | NumPy - Basics
Topic: Array Creation, Shape, Indexing, Math Operations
"""

import numpy as np

# ─────────────────────────────────────────────
# QUESTIONS
# ─────────────────────────────────────────────

# Q1. Create a 1D NumPy array of numbers 1 to 10.
arr = np.arange(1, 11)
print("Q1:", arr)

# Q2. Create a 3x3 matrix of zeros and ones.
print("Q2 Zeros:\n", np.zeros((3, 3)))
print("Q2 Ones:\n", np.ones((3, 3)))

# Q3. Create an identity matrix of size 4x4.
print("Q3:\n", np.eye(4))

# Q4. Find the shape, size, and data type of an array.
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print("Q4 Shape:", arr2d.shape, "| Size:", arr2d.size, "| Dtype:", arr2d.dtype)

# Q5. Reshape a 1D array of 12 elements into a 3x4 matrix.
flat = np.arange(1, 13)
reshaped = flat.reshape(3, 4)
print("Q5:\n", reshaped)

# Q6. Perform element-wise addition, subtraction, multiplication on two arrays.
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])
print("Q6 Add:", a + b, "| Sub:", a - b, "| Mul:", a * b)

# Q7. Find the sum, mean, median, and standard deviation of an array.
data = np.array([4, 7, 13, 2, 1, 9, 6])
print("Q7 Sum:", np.sum(data), "| Mean:", np.mean(data))
print("    Median:", np.median(data), "| Std:", np.std(data).round(2))

# Q8. Get all elements greater than 5 from an array (Boolean Indexing).
arr = np.array([1, 8, 3, 7, 5, 9, 2])
print("Q8:", arr[arr > 5])

# Q9. Stack two arrays vertically and horizontally.
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
print("Q9 Vertical:\n", np.vstack([x, y]))
print("Q9 Horizontal:", np.hstack([x, y]))

# Q10. Generate 5 random integers between 0 and 100.
random_vals = np.random.randint(0, 100, size=5)
print("Q10:", random_vals)
