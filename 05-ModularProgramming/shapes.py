import turtle
def drawSquare(x,y,n):
    skr= turtle.Turtle()
    skr.penup()
    skr.setposition(x,y)
    skr.pendown()
    for i in range(4): 
        skr.forward(n) 
        skr.right(90)     