def count_frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

if __name__ == '__main__':
    text = 'hello world'
    print(f'String: \'{text}\'')
    print(f'Frequency: {count_frequency(text)}')
