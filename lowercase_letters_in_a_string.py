s=input()
ns="abcdefghijklmnopqrstuvwxyz"
c=0
for i in s:
    if i in ns:
        c+=1
print(c)