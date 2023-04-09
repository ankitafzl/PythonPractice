# ask a user for name
# example - Ankush  Singh
# print count of each words
# output:
#      A : 1
#      n : 2
#      k : 1
#      u : 1 
#      s : 2
#      h : 2
#      g : 1
#        : 1
#      i : 1 

tem_var=""
name=input("please enter your name : ")
i=0
while i<len(name):
    if name[i] not in tem_var:
        tem_var += name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    i+=1
