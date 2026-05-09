# Q23. Write a program to print a pyramid pattern of numbers and 
# calculate the sum of all numbers printed in the pattern.

def number_pyramid(rows):
    total_sum = 0
    for i in range(1, rows + 1):
        print(" " * (rows - i), end="")
        for j in range(1, i + 1):
            print(j, end=" ")
            total_sum += j
        print()
    print(f"Sum of all numbers: {total_sum}")

if __name__ == "__main__":
    number_pyramid(4)

# Expected Output:
#    1 
#   1 2 
#  1 2 3 
# 1 2 3 4 
# Sum of all numbers: 20
