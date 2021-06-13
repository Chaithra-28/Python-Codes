s= input()
d= ''
e= ''
i=0
for c in range(len(s)):
    if i%2==0:
        d+=s[i]
    else:
        e+=s[i]
    i+=1
print(d+' '+e)