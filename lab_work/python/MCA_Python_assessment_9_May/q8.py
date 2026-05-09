# Q8. Write a Python program to perform union, intersection, 
# symmetric difference, and subset operations on two sets entered by the user.

def set_ops(a, b):
    print(f"Union: {a | b}")
    print(f"Intersection: {a & b}")
    print(f"Sym Diff: {a ^ b}")
    print(f"Is Subset (A in B): {a.issubset(b)}")

if __name__ == "__main__":
    set_ops({1,2,3}, {3,4,5})

# Expected Output:
# Union: {1, 2, 3, 4, 5}
# Intersection: {3}
# Sym Diff: {1, 2, 4, 5}
# Is Subset (A in B): False
