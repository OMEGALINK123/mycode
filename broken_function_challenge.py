#!/usr/bin/env python3
import random

num= input("How many Shakespearean insults would you like?")

insult_list= open("/home/student/mycode/insults.txt", "r")
insult= insult_list.readline()


def insult_generator(num):
    print("You are a", end="")
    for x in num:
      print(random.choice(insults))

insult_generator(num)
