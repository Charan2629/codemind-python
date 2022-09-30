s=input()
a=''
for i in s:
    if i in "aeiou":
        a=a+i
r="".join(set(a))
if len(r)==5:
    print(True)
else:
    print(False)