def first_unique(s):
    if s == '':
        return -1

    for item in s:
        if s.count(item) == 1:
            return s.index(item)
            break

    return -1
s=input()
print(first_unique(s))