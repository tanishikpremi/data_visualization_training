a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

def find_largest(a, b, c):
    if a > b and a > c:
        return "a is the largest"
    elif b > a and b > c:
        return "b is largest"
    elif a == b == c:
        return "All are equal"
    else:
        return "c is largest"

# Since the function 'returns' the value, we have to print the result of the call
result = find_largest(a, b, c)
print(result)