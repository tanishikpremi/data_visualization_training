# Q28. Develop a menu-driven mathematical utility program using functions 
# for factorial, prime checking, and Armstrong number checking.

import math

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def is_armstrong(n):
    return n == sum(int(d)**len(str(n)) for d in str(n))

def math_utility():
    actions = [(1, 5), (2, 7), (3, 153), (4, 0)] # Simulated input
    for choice, num in actions:
        if choice == 1: print(f"Factorial of {num}: {math.factorial(num)}")
        elif choice == 2: print(f"{num} is Prime: {is_prime(num)}")
        elif choice == 3: print(f"{num} is Armstrong: {is_armstrong(num)}")
        elif choice == 4: break

if __name__ == "__main__":
    math_utility()

# Expected Output:
# Factorial of 5: 120
# 7 is Prime: True
# 153 is Armstrong: True
