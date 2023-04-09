# def solve(s):
#     return ' '.join(i.capitalize()  for i in s.split(' '))
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     s = input()

#     result = solve(s)

#     fptr.write(result + '\n')

#     fptr.close()

#the minion game

def minion_game(string):
    # your code goes here
    s1=0
    s2=0
    vow='AEIOU'
    for i in range(len(s)):
        if s[i] not in vow:
            s1=s1+(len(s)-i)
        else:
            s2=s2+(len(s)-i)
    if s1>s2: 
        print("Stuart",s1)
    elif s2>s1:
        print("Kevin",s2)
    else:
        print("Draw")                

if __name__ == '__main__':
    s = input()
    minion_game(s)