# Q3. Create a program that generates the first N prime numbers using a for loop 
# and also calculates the sum and average of those prime numbers.

def n_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime: primes.append(num)
        num += 1
        
    total = sum(primes)
    avg = total / n if n > 0 else 0
    print(f"Primes: {primes}\nSum: {total}\nAverage: {avg:.2f}")

if __name__ == "__main__":
    n_primes(5)

# Expected Output:
# Primes: [2, 3, 5, 7, 11]
# Sum: 28
# Average: 5.60
