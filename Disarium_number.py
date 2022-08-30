n=int(input())
Sum,p=0,1
for i in str(n):
    Sum+=int(i)**p
    p+=1
if Sum==n:
    print(True)
else:
    print(False)