import time
import random
from random import *

# get names
print("you are about to listen to story, i will be your narator")
time.sleep(1)
print("to get started with...")
time.sleep(1)
print("what friends would like to have an adventure? (input list of names separated by a comma)")
my_input = input(">>")
names =my_input.split(",")

# base stories
my_stories = [" and jill went up the hill",
              " drove off into the sunset",
              " got to pymaster first",
              " thinks break is not a virus"]
# braches off base stories
my_substories = [[" and fetched a pail", " and got icecream", " and contracted a waterborne illness", " and broke their necks", " and got mauled by a wolf"],
                 [" to get a bottle of milk and dinner", " but crashed just outside of your view", " in a super fancy car going at 150 miles per hour" , " to go see grandma"],
                 [" and created super hard challenges that people could barely finish", " and created very easy challenges that taught concepts easily, and allowed people freedom to design.", " and never was heard from again"],
                 [" and got lynched by the coding community at large", " and also has never tried to use break before", " and also isn't a coder"]]

                    #substory one
my_subsubstories = [[[" to get some water, milk and juice from the market", " to clean up the evidence", " for grandma"],
                     [" which was posioned", "which was delicious", " which was the wrong flavor", " which was melted", " which was homemade"],
                     [" but you were cured", ", you got dysentery... good luck", " but it is harmless... for now", " but it is harmless"],
                     [" they were rushed to the hospital, and made a full recovery", " and were just left there to rot", "and lived the rest of their short life in agony"],
                     [" and was never found again", " and lost their eyes", "but fended off the wolf", ", luckely, jill had a spare 2 by 4"]],
                    #sub story 2
                     [[ " but the milk was poisoned", " but the dinner was posioned", ", it was delicious", " but they crahsed on the way back"],
                     [" you really don't want to see the crash site", ", no one was hurt", ", a full recovery was made", ", rip car"],
                     [", a cop spotted the car, rip drivers licence", " the driver was good enough not to crash, suprising", " right off a clif"],
                     [", grandma didn't remember who s/he was, she called the cops", " but s/he forgot where grandma's house was"]],
                    #substory 3
                     [[ " and from that day people hated s/he", " and made everyone a master coder in no time", " and was never heard from again"],
                     [" and was revered in all the land for his/hers mercy and amazing projects", " and was a major slacker", " and geve everybody half points no mater what"],
                     [ ", i don't think an explaination is needed on this one"]],
                    #substory 4
                     [[" and by the coding community, i mean james"],
                     [ " because they are a smart coder that knows what they are doing", " because they have no idea what a computer is", " becuase they have a life"],
                     [" because they have a life, ewww", " because they are normal", " because they live in north korea"]]]
# print a story for every name
for name in names:
    # get a random number <= number of base stories
    rand = randint(0, len(my_stories) - 1)
    rand2 = randint(0, len(my_substories) - 1)
    # gets the story based on random number
    story = my_stories[rand]
    substory = my_substories[rand] [rand2]
    subsubstory = choice(my_subsubstories [rand] [rand2])
    # prints the inputed name, and the story, and generates the substory to print
    print(name + story + substory + subsubstory)