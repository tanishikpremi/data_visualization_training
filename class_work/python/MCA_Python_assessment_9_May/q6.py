# Q6. Write a Python program to merge two lists, remove duplicate values, 
# sort the final list in descending order, and display only those numbers 
# that are divisible by both 3 and 5.

def merge_and_process(l1, l2):
    merged = list(set(l1 + l2))
    merged.sort(reverse=True)
    div_by_15 = [x for x in merged if x % 15 == 0]
    
    print(f"Merged & Sorted: {merged}")
    print(f"Divisible by 3 and 5: {div_by_15}")

if __name__ == "__main__":
    merge_and_process([15, 30, 5], [60, 15, 22])

# Expected Output:
# Merged & Sorted: [60, 30, 22, 15, 5]
# Divisible by 3 and 5: [60, 30, 15]
