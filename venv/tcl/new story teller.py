import time
import random
from random import *
print("you are about to play a choose your own adventure style story, i will be your narator")
print("to get started with...")
print("what is your name?")
name = input(">>")
introduction = ['i have heard that name before', 'that is a odd name', 'that is a nice name', 'wow, i already dislike you because of your name']
introduction2 = ['anyway, back to the story', '*wonders why that name exists*', 'well, here goes nothing']
secure_random = random.SystemRandom()
print(name + "...")
for x in range(0, 1):
    print(secure_random.choice(introduction))
    print(secure_random.choice(introduction2))