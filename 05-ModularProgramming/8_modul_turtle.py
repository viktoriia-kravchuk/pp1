import turtle
def drawSquare(x,y,n):
    skr= turtle.Turtle()
    skr.penup()
    skr.setposition(x,y)
    skr.pendown()
    for i in range(4): 
        skr.forward(n) 
        skr.right(90)     
for i in range(4):
    for j in range(4):
        drawSquare(-200+i*100, 200-j*100, 100)  