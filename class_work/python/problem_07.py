def remove_duplicates(lst):
    result = []
    seen = set()
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

if __name__ == '__main__':
    nums = [1, 2, 2, 3, 4, 4, 5]
    print(f'Original: {nums}')
    print(f'Without duplicates: {remove_duplicates(nums)}')
