import turtle

# set variables to refer to screen & turtle
wn = turtle.Screen()
tur = turtle.Turtle()
tur.shape("turtle")
tur.showturtle()

for i in range(18):
    tur.forward(20)
    tur.left(20) # turn left 20 degrees

turtle.mainloop() # make screen show
