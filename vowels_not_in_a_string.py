s=input()
c="aeiou"
a=[]
b=[]
flag=0
for i in s:
    if i in c:
        a.append(i)
for i in c:
    if i not in a:
        b.append(i)
        flag=1
if flag:
    print(*b)
else:
    print(0)