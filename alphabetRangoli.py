def print_rangoli(size):
    # your code goes here
    n=size
    list1=list(map(chr,range(97,123)))
    x=list1[n-1::-1]+list1[1:n]
    a=len('-'.join(x))
    for i in range(1,n):
        print('-'.join(list1[n-1:n-i:-1]+list1[n-i:n]).center(a,'-'))
    for i in range(n,0,-1):
        print('-'.join(list1[n-1:n-i:-1]+list1[n-i:n]).center(a,'-'))    

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)