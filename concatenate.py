import numpy
n,m,p=map(int,input().split())
str1=[list(map(int,input().split())) for i in range(n)]
str2=[list(map(int,input().split())) for i in range(m)]
arr1=numpy.array(str1)
arr2=numpy.array(str2)
print(numpy.concatenate((arr1,arr2),axis=0))
