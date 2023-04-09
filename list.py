N = int(input())
list=[]
for i in range(0,N):
        l=input().split()
        if l[0]=="print":
            print(list)
        elif l[0]=="insert":
            list.insert(int(l[1]),int(l[2]))
        elif l[0]=="remove":
            list.remove(int(l[1]))
        elif l[0]=="pop":
            list.pop()
        elif l[0]=="append":
            list.append(int(l[1])) 
        elif l[0]=="sort":
            list.sort()
        else:
            list.reverse()           