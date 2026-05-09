# Q19. Write a function that accepts a list of integers and returns 
# a new list containing factorial of only even numbers.

import math

def even_factorials(lst):
    return [math.factorial(x) for x in lst if x % 2 == 0]

if __name__ == "__main__":
    print(even_factorials([1, 2, 3, 4, 5]))

# Expected Output:
# [2, 24]
