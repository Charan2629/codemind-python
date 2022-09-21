def is_perfect(n):
    sq=n**0.5
    if sq==int(sq):
        return 1
    else:
        return 0
def fib(n):
    if is_perfect(5*n*n+4) or is_perfect(5*n*n-4):
        return True
    else:
        return False
n=int(input())
print(fib(n))