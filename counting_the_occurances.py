s = input()
p=input()
c=0
flag=0
for i in s:
    if i==p:
        c+=1
        flag=1
if flag==1:
    print(c)
else:
    print('-1')