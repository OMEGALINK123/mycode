#!/usr/bin/env python3

import re



def calculator(int1, int2, symbol):



    if symbol == "+":
        answer=(int1 + int2)
        print("Answer: ", answer)
    elif symbol == "-":
        answer=(int1 - int2)
        print("Answer: ", answer)
    elif symbol == "*":
        answer=(int1 * int2)
        print("Answer: ", answer)
    elif symbol == "/":
        answer=(int1 / int2)
        print("Answer: ", answer)
    print(" ")
    print("enjoy\n")

    file_creator(answer):

def file_creator(answer):

    with open("answer.txt", "a") as answerfile:

        print('Here is your answer: ', answer, file=answerfile)



while True:
        try:
            int1 = float(input("Enter first number: "))
            int2 = float(input("Enter second number: "))
            symbol = input("Enter an operator you want to use\n + \n -\n *\n / \n""Input: ")
            if not re.match("[+*/-]", symbol):
                print("That's not what I asked try again ")
            else:
                calculator(int1, int2, symbol)
                break
        except:
            print("Try again ")
