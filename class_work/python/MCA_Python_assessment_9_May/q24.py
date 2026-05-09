# Q24. Create a function for division of two numbers and use 
# exception handling to validate inputs and avoid runtime errors.

def safe_divide(a, b):
    try:
        a, b = float(a), float(b)
        return a / b
    except ValueError:
        return "Error: Invalid numeric input."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

if __name__ == "__main__":
    print(safe_divide(10, 2))
    print(safe_divide(10, 0))
    print(safe_divide("a", 2))

# Expected Output:
# 5.0
# Error: Cannot divide by zero.
# Error: Invalid numeric input.
