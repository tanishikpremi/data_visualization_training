# Q1. Write a Python program that accepts a paragraph from the user and calculates the number of 
# uppercase letters, lowercase letters, digits, spaces, and special characters. 
# Display the result in descending order based on frequency.

def count_characters(paragraph):
    counts = {'lowercase': 0, 'uppercase': 0, 'digits': 0, 'spaces': 0, 'special_chars': 0}
    
    for char in paragraph:
        if char.islower(): counts['lowercase'] += 1
        elif char.isupper(): counts['uppercase'] += 1
        elif char.isdigit(): counts['digits'] += 1
        elif char.isspace(): counts['spaces'] += 1
        else: counts['special_chars'] += 1
            
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    
    print("Character Frequencies (Descending Order):")
    for char_type, count in sorted_counts:
        print(f"{char_type}: {count}")

if __name__ == "__main__":
    sample = "Hello World! 2026..."
    print(f"Input: {sample}")
    count_characters(sample)

# Expected Output:
# Input: Hello World! 2026...
# Character Frequencies (Descending Order):
# lowercase: 8
# spaces: 2
# uppercase: 2
# special_chars: 4
# digits: 4
