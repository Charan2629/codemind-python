s=input().split()
c=0
a=[]
for i in s:
    for j in i:
        if j in "aeiouAEIOU":
            c+=1
    a.append(c)
    c=0
print(*a)