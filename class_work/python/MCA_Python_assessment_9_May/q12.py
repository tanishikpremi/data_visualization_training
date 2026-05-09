# Q12. Develop a calculator program that handles division by zero, 
# invalid inputs, and incorrect operations using multiple exception blocks.

def calculator(a, b, op):
    try:
        a, b = float(a), float(b)
        if op == '+': return a + b
        elif op == '-': return a - b
        elif op == '*': return a * b
        elif op == '/': return a / b
        else: raise ValueError("Invalid operation")
    except ZeroDivisionError: return "Error: Division by zero"
    except ValueError as e: return f"Error: {e}"
    except Exception as e: return f"Unexpected Error: {e}"

if __name__ == "__main__":
    print(calculator(10, 0, '/'))
    print(calculator(10, 5, '%'))
    print(calculator("a", 5, '+'))

# Expected Output:
# Error: Division by zero
# Error: Invalid operation
# Error: could not convert string to float: 'a'
