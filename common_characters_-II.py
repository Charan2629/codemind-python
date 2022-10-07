a=list(input().lower().replace(' ',''))
b=list(input().lower().replace(' ',''))
d=[]
c=0
for i in a:
    if i in b and i not in d:
        d.append(i)
        c+=1
print(c)