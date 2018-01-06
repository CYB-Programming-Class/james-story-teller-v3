# https://codereview.stackexchange.com/questions/22822/simple-quiz-program <- used as a guide
# all code hand written, then copied for questions and mostly understood, comments still added though
stop1 = False
stop2 = False
stop3 = False
stop4 =  False
stopbonus = False
print("gamer quiz")
score = 0
#                                                                    QUESTION 1
question1 = "which is better?"
options1 = "a. pc\nb. console\n"
# ^ varibles for the first question and answer
print(question1)
print(options1)
# ^ prints question and answers
while stop1 == False:
    response = input("Hit 'a' or 'b' for your answer\n")
# ^ says to input your answer
    if response ==  "a":    print   ("correct")
    score + 1
    stop1 = True
# ^ break will skip else statment
else:
    print("WRONG")
    while stop1 == False:
            response = input("Hit 'a' or 'b' for your answer\n")
# asks question again
            if response == "a":
                print ("correct")
                stop1 = True
            else:
                print("incorrect")
                response = input("Hit 'a' or 'b' for your answer\n")
                if response == "a":
                    print("correct")
                    stop1 = True
    else: print ("Incorrect, the correct answer was pc")
    stop1 = True
# shows you that you have failed the question, goes to next

# ^ if answer was correct, it goes to the next question
#code is a repeat with changed variables from here on out for the two other questions
#                                                                       QUESTION 2
question2 = "which is better?"
options2 = "a. using steam for games\nb. using disks for games\n"
# ^ varibles for the second question and answer
print(question2)
print(options2)
# ^ prints question and answers
while stop2 == False:
    response = input("Hit 'a' or 'b' for your answer\n")
# ^ says to input your answer
    if response == "a":
        print ("correct\n")
    score + 1
    stop2 = True
else:
    print ("incorrect")
while stop2 == False:
    if response == "a": print("correct\n")
    stop2 = True
else:
    print("WRONG, GET WITH THE TIMES")
while stop2 == False:
            response = input("Hit 'a' or 'b' for your answer\n")
# asks question again
            if response == "a": print("correct")
            stop2    =  True
else:
    while stop2 == False:
        response = input("Hit 'a' or 'b' for your answer\n")
# asks question again
        if response == "a": print("correct")
        stop2 = True
    print("Incorrect,the answer was steam")
    stop2    =   True
# ^ if answer was correct, it goes to the next question
#                                                              QUESTION 3
question3 = "Who is the head of valve?"
options3 = "a. Gabe Newell\nb. Bill Gates\n c. Warren Buffet\n"
# ^ varibles for the third question and answer
print(question3)
print(options3)
# ^ prints question and answers
while stop3 == False:
    response = input("Hit 'a', 'b' or 'c' for your answer\n")
# ^ says to input your answer
    if response == "a":
        print ("correct")
        score + 1
        stop3 = True
# ^ break will skip else statment
    else:
        print("WRONG")
        while stop3 == False:
            response = input("Hit 'a', 'b' or 'c' for your answer\n")
# asks question again
            if response == "a":
                print ("correct")
                stop3 = True
            else:
                print("incorrect")
while stop3 == False:
    response = input("Hit 'a' or 'b' for your answer\n")
            # asks question again
    if response == "a": print("correct")
    stop3 = True
else:
    print("incorrect, the correct answer was Gabe Newell")
# ^ if answer was correct, it goes to the next question
#next question made from memory
#                                                       question 4
while stop4 == False:
    print ("what do you want more, half life three, or the next cod game?")
    print ("a. half life three\nb. the next cod game\n")
    input = ("hit 'a', or 'b'")
if response == "y":
    print("correct you glorious person")
    score + 1
    stop4 = True
else:
    print("try again")
    input = ("hit 'a', or 'b'")
if response == "y":
    print("correct")
    stop4 = True
else:
    print ("try again")
    while stop == False:
        response = input("Hit 'a' or 'b' for your answer\n")
        # asks question again
        if response == "a": print("correct")
        stop4 = True
    else:
        print("the correct answer was half life three")
    stop4 = True



#  bonus question
while stopbonus == False:
            extra = input("do you want a bonus question for extra credit?\nhit 'y' or 'n'\n")

            if extra == "y":
                print("is skyrim...")
                print("a. a good game\nb. a bad game")

                while stopbonus == False:
                    response = input("hit 'a' or 'b'\n")

                    if response == "a":
                        score + 1
                        stopbonus = True
                    else:
                        print("Incorrect!!! Try again.")

                    while stopbonus == False:
                        response = input("Hit 'a'or 'b'\n")

                        if response == "a":
                            stopbonus = True
                        else:
                            print("no, educate yourself")
                            stopbonus = True
            elif extra == "n":
                stopbonus = True
            else:
                print("only hit 'y' or 'n', you lost your chance at the bonus")
print (score)