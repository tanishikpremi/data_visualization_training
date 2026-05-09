# Q34. Write a program to encrypt a message using Caesar Cipher technique 
# and decrypt it back to the original message.

def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode == 'decrypt': shift = -shift
        
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

if __name__ == "__main__":
    msg = "Hello World!"
    encrypted = caesar_cipher(msg, 3, 'encrypt')
    decrypted = caesar_cipher(encrypted, 3, 'decrypt')
    
    print(f"Original: {msg}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")

# Expected Output:
# Original: Hello World!
# Encrypted: Khoor Zruog!
# Decrypted: Hello World!
