def first_non_repeating(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    for char in s:
        if freq[char] == 1:
            return char
    return None

if __name__ == '__main__':
    text = 'swiss'
    print(f'String: \'{text}\'')
    print(f'First non-repeating character: {first_non_repeating(text)}')
