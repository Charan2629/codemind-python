n=input()
v,s,d,c=0,0,0,0
for i in n:
    if i in 'aeiouAEIOU':
        v+=1
    
    if i in ' ':
        s+=1
    if i in '0123456789':
        d+=1
    if i not in 'aeiouAEIOU 0123456789':
        c+=1
print('Vowels:',v)
print('Consonants:',c)
print('Digits:',d)
print('White spaces:',s)