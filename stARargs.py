# make flexible functions
# operator
# args

def all_total(*args):
    print(args)
all_total(1,2,3,4,5)    

def add_total(*args):
    total=0
    for num in args:
        total+=num
    return total
print(add_total(1,2,3,4,5))  

######################### args with normal parameter #############

def multiply_nums(*args):
    multiply=1
    print(args)
    for i in args:
        multiply*=i
    return multiply
print(multiply_nums(2,3,4))    

def multiply_nums1(num,*args):
    multiply=1
    print(num)
    print(args)
    for i in args:
        multiply*=i
    return multiply
print(multiply_nums1(2,3,4)) 

################# args as arguments #############

def multiply_nums2(*args):
    multiply=1
    print(args)
    for i in args:
        multiply*=i
    return multiply
nums=[2,3,4]   
print(multiply_nums2(*nums)) 

