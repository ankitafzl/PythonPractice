import numpy
n,m=map(int,input().split())
str1=numpy.array([input().strip().split() for _ in range(n)],int)
print(str1.transpose())
print(str1.flatten())
