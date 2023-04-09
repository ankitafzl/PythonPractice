n=[tuple(input().split())for _ in range(int(input()))]
# def sortList(num):
#    return int(num[1])
# print(sorted(n,key=sortList))

print(sorted(n,key=lambda x:int(x[1])))
