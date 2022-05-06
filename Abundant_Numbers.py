n=int(input())
Sum=1
temp=n
for i in range (2,n) :
    if n%i==0:
        Sum=Sum+i
if Sum > temp :
    print(True)
else :
    print(False)