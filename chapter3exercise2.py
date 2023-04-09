# exercise-watch Coco
# ask user's name  and age
# if user's name start with ('a' or 'A') and age is above  10 then
# print 'you can watch coco movie'
# else print 'sorry, you cannot watch coco' 

name=input("Enter user's name : ")
age=int(input("Enter your age : "))
if (name[0]=='a' or name[0]=='A') and  age>=10:
    print(" You can watch coco movie ")
else:
    print("sorr, you cannot watch coco")   
