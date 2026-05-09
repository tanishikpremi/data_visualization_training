# Q18. Develop a frequency counter that stores occurrence of each word 
# from a paragraph into a dictionary and displays the most repeated word.

def most_repeated(text):
    words = text.lower().replace('.', '').split()
    counts = {}
    for w in words: counts[w] = counts.get(w, 0) + 1
    most_freq = max(counts, key=counts.get)
    return most_freq, counts[most_freq]

if __name__ == "__main__":
    para = "This is a test. This test is only a test."
    w, c = most_repeated(para)
    print(f"Most repeated word: '{w}' ({c} times)")

# Expected Output:
# Most repeated word: 'test' (3 times)
