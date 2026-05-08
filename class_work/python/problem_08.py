def swap_dict(d):
    return {v: k for k, v in d.items()}

if __name__ == '__main__':
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    print(f'Original: {my_dict}')
    print(f'Swapped: {swap_dict(my_dict)}')
