def sort_by_marks(students):
    return sorted(students, key=lambda x: x[1])

if __name__ == '__main__':
    data = [('Alice', 85), ('Bob', 92), ('Charlie', 78)]
    print(f'Original: {data}')
    print(f'Sorted: {sort_by_marks(data)}')
