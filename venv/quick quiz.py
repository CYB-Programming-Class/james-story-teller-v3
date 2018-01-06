score = 0
stop = False
stop2 = False
stop3 = False
print("Here is a quiz")
print()
print()
print("Question 1")
print("what is 1 + 1?")
print()
print("a. 1")
print("b. 2")
print("c. 3")
while stop == False:
    answer = input("Make your choice:\n ")
    if answer == "b":
        print("Correct!")
        score = score + 1
        stop = True
    else:
        print("incorrect or invalid input, please try again")
        answer = input("Make your choice: ")
        if answer == "b":
            print("Correct!")
            stop = True
        else:
            print("incorrect, the correct answer was b")
            stop = True
#-------------------------------------------------
print()
print()
print("Question 2")
print("what is 7+7?")
print()
print("a. 18")
print("b. 14")
print("c. 1")
while stop2 == False:
    answer = input("Make your choice:\n ")
    if answer == "b":
        print("Correct!")
        score = score + 1
        stop2 = True
    else:
        print("incorrect or invalid input, please try again")
        answer = input("Make your choice: ")
        if answer == "b":
            print("Correct!")
            stop2 = True
        else:
            print("incorrect, the correct answer was b")
            stop2 = True
#-----------------------------------------------------------------
print()
print()
print("Question 3")
print("which is better...?")
print()
print("a. console")
print("b. pc")
while stop3 == False:
    answer = input("Make your choice:\n ")
    if answer == "b":
        print("Correct!")
        score = score + 1
        stop3 = True
    else:
        print("incorrect or invalid input, please try again")
        answer = input("Make your choice: ")
        if answer == "b":
            print("Correct!")
            stop3 = True
        else:
            print("incorrect, the correct answer was b")
            stop3 = True


print("your score out of 3 is...")
print (score)

