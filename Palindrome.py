def is_palin(n):
    if str(n)==str(n)[::-1]:
        return True
    else:
        return False
n=int(input())
print(is_palin(n))