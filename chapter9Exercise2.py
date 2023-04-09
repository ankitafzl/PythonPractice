# num to string 
# define a function

# example
# input -------> [True,False,[1,2,3],1,1.0,3]
# output ------>['1','1.0','3']

def num_type(l):
    return [str(i) for i in l if (type(i)==int or type(i)==float)]
print(num_type([True,False,[1,2,3],1,1.0,3]))    
