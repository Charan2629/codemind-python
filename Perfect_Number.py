n=int(input())
Sum=0
for i in range(1,n//2+1):
    if n%i==0:
        Sum+=i
if Sum==n:
    print(True)
else:
    print(False)