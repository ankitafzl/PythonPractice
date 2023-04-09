from collections import Counter
num1=int(input())
list1=map(int,input().split())
num2=input(input())
shoes=Counter(list1)
income=0
for i in range (num2):
    size,price=map(int,input().split())
    if shoes[size]:
        income+=price
        shoes[size]-=1
print(income)        
