import math
def is_perfect(n):
    root=math.sqrt(n)
    if int(root + 0.5) ** 2 == n:
        return 1
    else:
        return 0
n=int(input())
Sum=0
l=list(map(int,input().split()))
for i in l:
    if is_perfect(i)==1:
        Sum=Sum+i
print(Sum)