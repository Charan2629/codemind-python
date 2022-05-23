def sum_of_digits(n):
    s = 0

    while n:
        s += n % 10
        n //= 10

    if s > 9:
        return sum_of_digits(s)

    return s

n = int(input())
print(sum_of_digits(n))