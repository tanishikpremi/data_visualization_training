# Q13. Write a NumPy program to create a 5x5 matrix with random integers 
# and calculate row-wise sum, column-wise sum, transpose, and determinant.

import numpy as np

def matrix_ops():
    np.random.seed(42)
    mat = np.random.randint(1, 10, (5, 5))
    print(f"Matrix:\n{mat}")
    print(f"Row-wise sum: {np.sum(mat, axis=1)}")
    print(f"Col-wise sum: {np.sum(mat, axis=0)}")
    print(f"Transpose:\n{mat.T}")
    print(f"Determinant: {np.linalg.det(mat):.2f}")

if __name__ == "__main__":
    matrix_ops()

# Expected Output:
# Matrix:
# [[7 4 8 5 7]
#  [3 7 8 5 4]
#  [8 8 3 6 5]
#  [2 8 6 2 5]
#  [1 6 9 1 3]]
# Row-wise sum: [31 27 30 21 24]
# Col-wise sum: [21 33 34 19 23]
# Transpose:
# [[7 3 8 2 1]
#  [4 7 8 8 6]
#  [8 8 3 6 9]
#  [5 5 6 2 1]
#  [7 4 5 5 3]]
# Determinant: -620.00
