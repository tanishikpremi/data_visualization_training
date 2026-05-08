# self learning - day 2
# topic: functions - defining, args, kwargs, lambda
# NOTE TO SELF: functions = reusable blocks, always use them instead of repeating code

# ── basic function ─────────────────────────────

def greet(name):
    return f"Hello, {name}!"

print(greet("Tanishik"))

# ── default arguments ──────────────────────────

def power(base, exp=2):
    return base ** exp

print(power(3))      # 9  (exp defaults to 2)
print(power(3, 3))   # 27

# ── *args - variable number of arguments ───────

def add_all(*nums):
    return sum(nums)

print(add_all(1, 2, 3))       # 6
print(add_all(10, 20, 30, 40)) # 100

# ── **kwargs - keyword arguments ───────────────

def student_info(**kwargs):
    for key, val in kwargs.items():
        print(f"  {key}: {val}")

student_info(name="Alice", age=21, city="Delhi")

# ── lambda - anonymous one-liner functions ─────
# honestly confused by these at first but they make sense now

square = lambda x: x ** 2
print(square(5))   # 25

# useful with sorted() and map()
nums = [5, 2, 8, 1, 9, 3]
print(sorted(nums, key=lambda x: -x))  # descending sort

doubled = list(map(lambda x: x * 2, nums))
print(doubled)

# filter - keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)

# ── recursion - factorial ──────────────────────
# tried to understand this, makes sense once you think about base case

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))   # 120
print(factorial(10))  # 3628800

# ── docstrings - good habit ────────────────────

def celsius_to_fahrenheit(c):
    """Converts Celsius to Fahrenheit.
    
    Args:
        c (float): Temperature in Celsius
    Returns:
        float: Temperature in Fahrenheit
    """
    return (c * 9/5) + 32

print(celsius_to_fahrenheit(100))  # 212.0
print(celsius_to_fahrenheit(0))    # 32.0
print(celsius_to_fahrenheit(37))   # 98.6
