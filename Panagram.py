s=input('Enter a String:')
s1='abcdefghijklmnopqrstuvwxyz'
s2=''
s=s.lower()
se=set(s)
l=list(se)
for i in l:
    if i==' ':
        l.remove(i)
l.sort()
for i in l:
    s2+=i

if(s1==s2):
    print('Sentence is Panagram')
else:
    print('Sentence is not Panagram')
