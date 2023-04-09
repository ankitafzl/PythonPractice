# take two comma separated inputs from user
# 1. user's name
# 2. a single character

# output - 2 print lines
# 1. user's name length
# 2. count the character that user inputed(bonus: case insenstive count)

name,char=input("Enter your name and character : ").split()
print(f"user\'s name length : {len(name)}")
#print(f"character count : {name.lower().count(char.lower())}")
print(f"character count : {name.strip().lower().count(char.strip().lower())}")




#"   Ankita   "----->" Ankita " ------->"ankita"
#" A " ------>"A"------> "a"

