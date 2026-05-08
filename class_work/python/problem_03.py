def find_common(list1, list2):
    common = []
    for item in list1:
        if item in list2 and item not in common:
            common.append(item)
    return common

if __name__ == '__main__':
    l1 = [1, 2, 3, 4, 5]
    l2 = [4, 5, 6, 7, 8]
    print(f'List 1: {l1}')
    print(f'List 2: {l2}')
    print(f'Common elements: {find_common(l1, l2)}')
