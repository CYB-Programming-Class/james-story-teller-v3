# https://codereview.stackexchange.com/questions/22822/simple-quiz-program <- used as a guide
# all code hand written, then copied for questions and mostly understood, comments still added though
stop = False
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
while stop == False:
    response = input("Hit 'a' or 'b' for your answer\n")
# ^ says to input your answer
    if response ==  "a":
        print   ("correct")
        score + 1
        stop = True
# ^ break will skip else statment
    if response
        print("WRONG")
        response = input("Hit 'a' or 'b' for your answer\n")
# asks question again
    if response == "a":
                print ("correct")
                stop = True
    else:
                print("incorrect")
                response = input("Hit 'a' or 'b' for your answer\n")
                if response == "a":
                    print("correct")
                    stop = True
                else: print ("Incorrect, the correct answer was pc, you console peasant")
    stop = True
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



print("your score out of 3 is...")
print (score)