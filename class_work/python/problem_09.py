def find_pairs(lst, target):
    pairs = []
    seen = set()
    for num in lst:
        complement = target - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)
    return pairs

if __name__ == '__main__':
    nums = [1, 5, 7, -1, 5]
    target_sum = 6
    print(f'List: {nums}, Target: {target_sum}')
    print(f'Pairs: {find_pairs(nums, target_sum)}')
