# exercise  one of three
# sum of n natural numbers
# ask a user for natural number(n)
# print total from 1 to n


n=int(input("You want to sum of which number : "))
total=0
i=1
while(i<=n):
    total+=i
    i+=1
print(total)    

n1=int(input("You want to start number : "))
n2=int(input("You want to last number : "))
total=0
i=n1
while(i<=n2):
    total+=i
    i+=1
print(total)    