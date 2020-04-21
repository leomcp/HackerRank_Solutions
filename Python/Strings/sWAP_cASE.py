def swap_case(s):
    new_s = ""
    for word in s:
        for char in word:
            if char.isupper():
                new_s = new_s + char.lower()
            else:
                new_s = new_s + char.upper()

    return new_s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)