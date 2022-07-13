n=int(input())
l=list(map(int,input().split()))
Sum=0
for i in l:
    Sum+=i
avg=Sum//n
if avg in l:
    print(True)
else:
    print(False)