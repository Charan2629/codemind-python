s=input().lower().replace(' ','')
a=[]
for i in s:
    if i not in a:
        a.append(i)
ns=sorted(a)
for i in ns:
    print(i,end='')