def is_armstrong(n):
    num_str = str(n)
    power = len(num_str)
    total = sum(int(digit) ** power for digit in num_str)
    return total == n

if __name__ == '__main__':
    num = 153
    print(f'Is {num} an Armstrong number? {is_armstrong(num)}')
