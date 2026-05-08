def flatten_list(nested):
    flat = []
    for item in nested:
        if isinstance(item, list):
            flat.extend(flatten_list(item))
        else:
            flat.append(item)
    return flat

if __name__ == '__main__':
    nested_data = [1, [2, [3, 4], 5], 6]
    print(f'Nested: {nested_data}')
    print(f'Flattened: {flatten_list(nested_data)}')
