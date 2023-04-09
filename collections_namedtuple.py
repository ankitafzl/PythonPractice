from collections import namedtuple
n=int(input())
data=namedtuple("data",input())
markslist=[]
for i in range(n):
    marks=int(data(*input().split()).MARKS)
    markslist.append(marks)
print(sum(markslist)/n)    