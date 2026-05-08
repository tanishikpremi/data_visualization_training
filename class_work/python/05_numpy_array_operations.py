"""
CLASS WORK | NumPy - Array Operations & Indexing
Topic: Slicing, Fancy Indexing, Linear Algebra, Broadcasting
"""

import numpy as np

# ─────────────────────────────────────────────
# QUESTIONS
# ─────────────────────────────────────────────

# Q1. Slice rows 1-2 and columns 0-1 from a 3x3 matrix.
mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Q1:\n", mat[1:3, 0:2])

# Q2. Replace all even numbers in an array with 0.
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
arr[arr % 2 == 0] = 0
print("Q2:", arr)

# Q3. Compute the dot product of two matrices.
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print("Q3 Dot Product:\n", np.dot(A, B))

# Q4. Find the transpose of a matrix.
print("Q4 Transpose:\n", A.T)

# Q5. Find eigenvalues and eigenvectors of a matrix.
eigenvalues, eigenvectors = np.linalg.eig(A)
print("Q5 Eigenvalues:", eigenvalues.round(2))

# Q6. Normalize an array so values are between 0 and 1.
raw = np.array([10, 20, 30, 40, 50], dtype=float)
normalized = (raw - raw.min()) / (raw.max() - raw.min())
print("Q6:", normalized)

# Q7. Use broadcasting to add a 1D array to each row of a 2D array.
grid = np.ones((3, 3))
row_add = np.array([1, 2, 3])
print("Q7:\n", grid + row_add)

# Q8. Sort an array and return the indices that would sort it (argsort).
data = np.array([50, 10, 40, 20, 30])
print("Q8 Sorted:", np.sort(data))
print("Q8 Argsort:", np.argsort(data))

# Q9. Stack three 1D arrays as columns in a 2D array.
col1 = np.array([1, 4, 7])
col2 = np.array([2, 5, 8])
col3 = np.array([3, 6, 9])
print("Q9:\n", np.column_stack([col1, col2, col3]))

# Q10. Compute cumulative sum of an array.
arr = np.array([1, 2, 3, 4, 5])
print("Q10:", np.cumsum(arr))
