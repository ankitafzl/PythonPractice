#list comprehension  with if statement

numbers=list(range(1,11))
print(numbers)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums=[]
for i in numbers:
    if i%2==0:
        nums.append(i)
print(nums)        

# even_nums=[i for i in numbers if i%2==0]
even_nums=[i for i in range(1,11) if i%2==0]
print(even_nums)

odd_nums=[i for i in range(1,11) if i%2!=0]
print(odd_nums)



