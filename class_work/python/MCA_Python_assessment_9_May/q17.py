# Q17. Create a program that checks whether numbers entered by the user 
# are Armstrong numbers using loops and conditional statements.

def is_armstrong(num):
    num_str = str(num)
    power = len(num_str)
    return sum(int(d) ** power for d in num_str) == num

if __name__ == "__main__":
    for n in [153, 370, 123]:
        print(f"{n} is Armstrong: {is_armstrong(n)}")

# Expected Output:
# 153 is Armstrong: True
# 370 is Armstrong: True
# 123 is Armstrong: False
