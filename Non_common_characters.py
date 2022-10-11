a=input().lower().replace(' ','')
b=input().lower().replace(' ','')
s=[]
c=0
for i in a:
    if i not in b:
        s.append(i)
for i in b:
    if i not in a:
        s.append(i)
ns=sorted(list(set(s)))
for i in ns:
    c+=1
print(c)