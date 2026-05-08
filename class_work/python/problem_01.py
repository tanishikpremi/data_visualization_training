def second_largest(lst):
    if len(lst) < 2:
        return None
    largest = float('-inf')
    second = float('-inf')
    for num in lst:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
    return second if second != float('-inf') else None

if __name__ == '__main__':
    nums = [10, 20, 4, 45, 99, 99]
    print(f'List: {nums}')
    print(f'Second largest: {second_largest(nums)}')
