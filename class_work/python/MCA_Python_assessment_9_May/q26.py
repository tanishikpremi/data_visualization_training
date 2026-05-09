# Q26. Write a program to separate vowels and consonants from a 
# sentence and store them in different lists.

def separate_chars(sentence):
    vowels_list = []
    consonants_list = []
    
    for char in sentence:
        if char.isalpha():
            if char.lower() in 'aeiou':
                vowels_list.append(char)
            else:
                consonants_list.append(char)
                
    return vowels_list, consonants_list

if __name__ == "__main__":
    v, c = separate_chars("Python Programming")
    print(f"Vowels: {v}")
    print(f"Consonants: {c}")

# Expected Output:
# Vowels: ['o', 'o', 'a', 'i']
# Consonants: ['P', 'y', 't', 'h', 'n', 'P', 'r', 'g', 'r', 'm', 'm', 'n', 'g']
