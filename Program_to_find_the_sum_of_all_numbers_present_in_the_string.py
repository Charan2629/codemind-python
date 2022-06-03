s=input()
Sum=0
for i in s:
    if i in '0123456789':
        Sum=Sum+int(i)
print(Sum)