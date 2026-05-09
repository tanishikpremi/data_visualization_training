# Q30. Write a NumPy program to create two matrices and perform 
# addition, subtraction, multiplication, and inverse operations.

import numpy as np

def matrix_arithmetic():
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])
    
    print("Addition:\n", a + b)
    print("Subtraction:\n", a - b)
    print("Multiplication:\n", np.dot(a, b))
    print("Inverse of A:\n", np.linalg.inv(a))

if __name__ == "__main__":
    matrix_arithmetic()

# Expected Output:
# Addition:
#  [[ 6  8]
#  [10 12]]
# Subtraction:
#  [[-4 -4]
#  [-4 -4]]
# Multiplication:
#  [[19 22]
#  [43 50]]
# Inverse of A:
#  [[-2.   1. ]
#  [ 1.5 -0.5]]
