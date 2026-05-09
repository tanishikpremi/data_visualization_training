# Q33. Create a program that copies contents from one file to another 
# and displays the total number of words copied.

def copy_file(source, destination):
    with open(source, 'w') as f:
        f.write("This is a sample text to be copied to another file.")
        
    try:
        with open(source, 'r') as src, open(destination, 'w') as dst:
            content = src.read()
            dst.write(content)
            
        words = len(content.split())
        print(f"Successfully copied {words} words from {source} to {destination}.")
    except FileNotFoundError:
        print("Source file not found.")

if __name__ == "__main__":
    copy_file('source.txt', 'destination.txt')

# Expected Output:
# Successfully copied 11 words from source.txt to destination.txt.
