# count=0
# num=int(input())
# for i in range(1,num+1):
#     if num%i==0:
#         count=count+i
# print(count)        


n=int(input())
l=[i for i in range(1,n+2) if n%i==0]
print(sum(l))