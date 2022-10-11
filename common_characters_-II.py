a=input().lower().replace(' ','')
b=input().lower().replace(' ','')
s=[]
c=0
for i in a:
    if i in b:
        s.append(i)
for i in list(set(b)):
    if i in list(set(s)):
        c+=1
print(c)