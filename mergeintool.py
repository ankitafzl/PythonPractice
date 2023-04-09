from collections import OrderedDict
def merge_the_tools(string, k):
    # your code goes here
    strlen=len(string)
    for i in range(0,strlen,k):
        print(''.join(OrderedDict.fromkeys(string[i:i+k])))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)


# import numpy
# poly=[float(n) for n in input().split()]
# n=float(input())
# print(numpy.polyval(poly,x))