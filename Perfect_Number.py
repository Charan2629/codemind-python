n=int(input())
Sum=0
for i in range(1,n):
    if n%i==0:
        Sum=Sum+i
if Sum==n:
    print(True)
else:
    print(False)