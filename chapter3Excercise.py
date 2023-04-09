# exercise, number guessing game
# make a variable , like winning_number and assign any number to it.
# ask your to guess a number
# if user guessed correctly  then print "You win !!!!"
# if user  didn't guessed correctly then:
#     if user guessed lower  than actual number  then print "too low"
#     if user guessed  higher than actual  number then print "too high"
######bonus###########
# google "how  to generate random number in python " to generate random
# winning number   

winning_number=30
guessed_number=int(input("guess a number between 1 and 100 : "))
if guessed_number==winning_number:
    print("You Win !!!!!")
else:
    if guessed_number<winning_number:
        print("too low")
    else:
        print("too high")    