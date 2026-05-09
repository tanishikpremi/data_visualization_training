# Q25. Store word frequencies from a text file into a dictionary 
# and display the top five most frequently used words.

from collections import Counter
import re

def top_five_words(filename):
    with open(filename, 'w') as f:
        f.write("apple banana apple orange apple banana grape grape orange apple grape")
        
    try:
        with open(filename, 'r') as f:
            words = re.findall(r'\b\w+\b', f.read().lower())
            freq = Counter(words)
            print("Top 5 Words:")
            for word, count in freq.most_common(5):
                print(f"{word}: {count}")
    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    top_five_words('word_freq.txt')

# Expected Output:
# Top 5 Words:
# apple: 4
# grape: 3
# banana: 2
# orange: 2
