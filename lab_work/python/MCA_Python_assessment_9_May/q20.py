# Q20. Create a file processing program that handles file not found errors 
# and counts total words, lines, and characters in a text file.

def process_file(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print(f"Lines: {len(content.splitlines())}")
            print(f"Words: {len(content.split())}")
            print(f"Characters: {len(content)}")
    except FileNotFoundError:
        print(f"Error: {filename} not found.")

if __name__ == "__main__":
    process_file("missing.txt")
    with open("sample.txt", "w") as f: f.write("Hello world\nFile.")
    process_file("sample.txt")

# Expected Output:
# Error: missing.txt not found.
# Lines: 2
# Words: 3
# Characters: 17
