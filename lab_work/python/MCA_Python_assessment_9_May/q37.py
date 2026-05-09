# Q37. Write a recursive function to calculate the sum of digits 
# of a given number and compare it with iterative approach.

def recursive_sum(n):
    if n == 0: return 0
    return (n % 10) + recursive_sum(n // 10)

def iterative_sum(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

if __name__ == "__main__":
    num = 12345
    print(f"Number: {num}")
    print(f"Recursive Sum: {recursive_sum(num)}")
    print(f"Iterative Sum: {iterative_sum(num)}")

# Expected Output:
# Number: 12345
# Recursive Sum: 15
# Iterative Sum: 15
