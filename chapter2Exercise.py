# ask user to input 3 numbers and you have to print average of three numbers using string formatting.
num1=input("enter the first number : ")
num2=input("enter the second number : ")
num3=input("enter the third number : ")
average=(int(num1)+int(num2)+int(num3))/3
print(average)
print("\t")

num1,num2,num3=input("enter the three numbers : ").split()
print(f"average of three numbers : {(int(num1)+int(num2)+int(num3))/3}")
 