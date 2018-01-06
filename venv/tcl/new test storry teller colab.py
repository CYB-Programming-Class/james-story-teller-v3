import time
import random
from random import *

# get names
print("you are about to listen to story, i will be your narator")
print("to get started with...")
print("what friends would like to have an adventure? (input list of names separated by a comma)")
my_input = input(">>")
names = my_input.split(",")

# print a single story
print(names[0] + " and jill went up a hill.")
my_stories = [" and jill went up a hill", " drove off into the sunset."]

# print a story for every name
for name in names:
    # print("hi " + name)
    # get a random number to select a random story
    # rand = randint(0, 2)
    # story = my_stories[rand] # get random story
    # print(name + story)
    # instead implement with choice function
    story = choice(my_stories)
    print(name + story)
    # print("you are being told story number" + str(rand))
