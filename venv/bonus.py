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