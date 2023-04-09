from collections import defaultdict
s=defaultdict(list)
list1=[]
m,n=map(int,input().split())
for i in range(m):
    a=input()
    s[a].append(i+1)
for i in range(n):
    b=input()
    list1=list1+[b]
for i in list1:
    if i in s:
        print(' '.join(map(str,s[i])))
    else:
        print(-1)            