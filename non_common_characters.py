a=input().lower().replace(' ','')
b=input().lower().replace(' ','')
s=[]
for i in a:
    if i not in b:
        s.append(i)
for i in b:
    if i not in a:
        s.append(i)
ns=sorted(list(set(s)))
for i in ns:
    print(i,end='')