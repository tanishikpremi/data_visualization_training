# Q5. Design a Python function that accepts a list of integers and returns the 
# second largest and second smallest element without using built-in sorting functions.

def second_extremes(arr):
    unique = list(set(arr))
    if len(unique) < 2: return None, None
    
    smallest = second_smallest = float('inf')
    largest = second_largest = float('-inf')
    
    for n in unique:
        if n > largest: second_largest, largest = largest, n
        elif n > second_largest: second_largest = n
        
        if n < smallest: second_smallest, smallest = smallest, n
        elif n < second_smallest: second_smallest = n
            
    return second_largest, second_smallest

if __name__ == "__main__":
    arr = [10, 5, 20, 8, 12]
    sec_l, sec_s = second_extremes(arr)
    print(f"List: {arr}\n2nd Largest: {sec_l}\n2nd Smallest: {sec_s}")

# Expected Output:
# List: [10, 5, 20, 8, 12]
# 2nd Largest: 12
# 2nd Smallest: 8
