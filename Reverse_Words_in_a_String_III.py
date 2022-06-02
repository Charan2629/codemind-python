string = input()
words = string.split(' ')
reverseWords = [word[::-1] for word in words]
reverseString = " ".join(reverseWords)
print(reverseString)