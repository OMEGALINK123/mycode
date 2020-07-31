#!/usr/bin/env python3
round = 0           # integer round initiated to 0
while True:        # sets up an infinite loop condition
    round = round + 1     
    print('What Superbowl did the Philidelphia Eagles beat the New England Patriots')
    answer = input("Your guess--> ")    # string ans collected from user
    if answer == '52': # logic to check if user gave correct answer
        print('Correct!')
        round = 0
        break             # break statement escapes the while loop
    elif round == 3:    # logic to ensure round has not yet reached 3
        print('Sorry, the answer was 52.')
        break             # break statement escapes the                 
                          # if answer was wrong, and round is not yet equal to 3
    if answer != '52':
        print("Wow, you're really not too bright!")

while True:
    round = round + 1

    print('What NFL team resides out of Seattle?')
    answer = input("Your guess--> ")
    
    if answer.lower() == 'seahawks': 

        print('Correct!')
        break

    elif round == 3:
        print('Sorry, the answer was the Seahawks.')
        break

    elif answer != 'Seahawks':
        print("Wow, you're not very smart are you?")










