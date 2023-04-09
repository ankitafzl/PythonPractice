from itertools import product
A=list(map(int,input().split(' ')))
B=list(map(int,input().split(' ')))
for i in product(A,B):
    print(i,end="")


print("\n")


#############itertools_permutation##################
# from itertools import permutations
# str1,p=input().split(' ')
# for i in list(permutations(sorted(str1),int(p))):
#     print(" ".join(i))    



#################itertools_combination##################
from itertools import combinations
str1,n=input().split()
n=int(n)
for i in range(1,n+1):
    for j in list(combinations(sorted(str1),i)):
        print("".join(j))