# self learning - day 1
# topic: strings and basic loops
# just getting comfortable again after a break

# ── string stuff ──────────────────────────────

name = "tanishik"
print(name.upper())         # TANISHIK
print(name.capitalize())    # Tanishik
print(len(name))            # 8

# reversing a string (cool trick)
print(name[::-1])  # kihsinat

# checking if something is in a string
sentence = "data science is awesome"
print("science" in sentence)   # True
print("math" in sentence)      # False

# string formatting - f-strings are cleaner than .format()
age = 22
print(f"My name is {name} and I am {age} years old")

# splitting and joining
csv_line = "alice,25,HR,Mumbai"
parts = csv_line.split(",")
print(parts)         # ['alice', '25', 'HR', 'Mumbai']
print(" | ".join(parts))   # alice | 25 | HR | Mumbai

# strip whitespace - useful for dirty data
raw = "   hello world   "
print(raw.strip())

# ── loops ─────────────────────────────────────

# for loop with range
for i in range(1, 6):
    print(i, end=" ")   # 1 2 3 4 5
print()

# while loop - sum until > 50
total = 0
n = 1
while total <= 50:
    total += n
    n += 1
print("Sum:", total, "| Steps:", n)

# enumerate - useful when you need index too
fruits = ["apple", "banana", "mango"]
for idx, fruit in enumerate(fruits, start=1):
    print(f"{idx}. {fruit}")

# TODO: practice zip() next time
# zip pairs two lists together - good for iterating two lists at once
names = ["Alice", "Bob", "Charlie"]
scores = [88, 72, 95]
for n, s in zip(names, scores):
    print(f"{n}: {s}")
