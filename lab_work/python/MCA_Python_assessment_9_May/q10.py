# Q10. Write a program to check whether a given string is a palindrome after 
# removing spaces, punctuation marks, and converting all characters to lowercase.

def is_palindrome(text):
    clean = "".join(c.lower() for c in text if c.isalnum())
    return clean == clean[::-1]

if __name__ == "__main__":
    text = "A man, a plan, a canal: Panama"
    print(f"'{text}' is Palindrome: {is_palindrome(text)}")

# Expected Output:
# 'A man, a plan, a canal: Panama' is Palindrome: True
