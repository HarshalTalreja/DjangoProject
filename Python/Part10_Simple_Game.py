###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:

# Try to figure out what this code is doing and how it might be useful to you
import random

print("Welcome Code Breaker! Let's see if you can guess my 3 digit number!")
digits = list(range(10))
random.shuffle(digits)
act_no = digits[:3]
print("Code has been generated, please guess a 3 digit number")
# print(act_no)
# Another hint:
guess = 0
guess = input("What is your guess? ")

while ((int(guess[0])!=act_no[0]) or (int(guess[1])!=act_no[1]) or (int(guess[2])!=act_no[2])):
    print("Here is the result of your guess:")
    if ((int(guess[0]) not in act_no) and (int(guess[1]) not in act_no) and (int(guess[2]) not in act_no)):
        print("Nope")
    else:
        if (int(guess[0])==act_no[0] or int(guess[1])==act_no[1] or int(guess[2])==act_no[2]):
            print("Match")
        else:
            print("Close")

    guess = input("What is your guess? ")
print("Congrats! You have breaked the Code")

# Think about how you will compare the input to the random number, what format
# should they be in? Maybe some sort of sequence? Watch the Lecture video for more hints!
