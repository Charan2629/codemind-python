s=input()
x,y=0,0
for i in s:
    if i in 'z':
        x+=1
    if i in 'o':
        y+=1
if 2*x==y:
    print('Yes')
else:
    print('No')