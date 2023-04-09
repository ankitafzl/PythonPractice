#center method
name="Ankita"
print(name.center(10,"*")) #### **Ankita**
n=input("Enter your name : ")
print(n.center(len(n)+8,"*"))

# Enter your name : nipu
# ****nipu****

################# strings  are mutable ################

string="string"
print(string[1])
new_string=string.replace('t','T')
print(new_string)