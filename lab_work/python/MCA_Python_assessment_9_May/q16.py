# Q16. Write a Python program using functions and loops to generate Fibonacci 
# numbers up to N and store only even Fibonacci numbers in a list.

def even_fibonacci(n):
    a, b = 0, 1
    even_fibs = []
    
    while a <= n:
        if a % 2 == 0:
            even_fibs.append(a)
        a, b = b, a + b
        
    return even_fibs

if __name__ == "__main__":
    print(f"Even Fibs up to 50: {even_fibonacci(50)}")

# Expected Output:
# Even Fibs up to 50: [0, 2, 8, 34]
