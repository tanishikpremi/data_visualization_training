# self learning - list comprehensions + sets
# these are SO much cleaner than regular for loops
# date: practicing on a weekend

# ── basic comprehension ────────────────────────

# old way
squares_old = []
for i in range(1, 11):
    squares_old.append(i**2)

# new clean way
squares = [i**2 for i in range(1, 11)]
print("Squares:", squares)

# with condition - only even squares
even_squares = [i**2 for i in range(1, 11) if i % 2 == 0]
print("Even squares:", even_squares)

# string operations with comprehension
words = ["hello", "world", "python", "is", "fun"]
upper_words = [w.upper() for w in words]
print(upper_words)

# nested comprehension - multiplication table 3x3
# kinda confusing at first but makes sense
table = [[i * j for j in range(1, 4)] for i in range(1, 4)]
for row in table:
    print(row)

# ── dict comprehension ─────────────────────────

# word lengths
word_lengths = {word: len(word) for word in words}
print(word_lengths)

# flip a dictionary (key becomes value)
original = {"a": 1, "b": 2, "c": 3}
flipped = {v: k for k, v in original.items()}
print("Flipped:", flipped)

# ── set comprehension ──────────────────────────

# unique characters in a string
sentence = "banana"
unique_chars = {char for char in sentence}
print("Unique chars:", unique_chars)  # order not guaranteed

# ── sets - i kept forgetting these exist ───────

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print("Union:", set_a | set_b)          # all elements
print("Intersection:", set_a & set_b)   # common elements
print("Difference:", set_a - set_b)     # in A but not B
print("Sym Diff:", set_a ^ set_b)       # in one but not both

# removing duplicates from a list using set
dupes = [1, 2, 2, 3, 3, 3, 4]
no_dupes = list(set(dupes))
print("No duplicates:", no_dupes)  # note: order may change

# checking membership - sets are FASTER than lists for this
# (important for large datasets)
big_set = set(range(1000000))
print(999999 in big_set)   # True - very fast
