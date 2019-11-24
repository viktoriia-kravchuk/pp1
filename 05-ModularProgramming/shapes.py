import turtle
def drawSquare(x,y,n):
    skr= turtle.Turtle()
    skr.penup()
    skr.setposition(x,y)
    skr.pendown()
    for i in range(4): 
        skr.forward(n) 
        skr.right(90)     
def drawCircle(x,y,r):
    skr= turtle.Turtle()
    skr.penup()
    skr.setposition(x,y)
    skr.pendown()
    skr.circle(r)  
def drawTriangle(x,y,m):
    skr= turtle.Turtle()
    skr.penup()
    skr.setposition(x,y)
    skr.pendown() 
    skr.right(60)
    skr.forward(m)
    for i in range(2):
        skr.right(120)
        skr.forward(m)
def drawStar():
    star=turtle.Turtle()
    for i in range(5):
        star.forward(200)
        star.right(144)      
def drawblackSquare(x,y,m):
    skr= turtle.Turtle()
    skr.penup()
    skr.setposition(x,y)
    skr.pendown()
    skr.color("black")
    skr.begin_fill()
    for i in range(4): 
        skr.forward(m) 
        skr.right(90)    
    skr.end_fill()

turtle.done()     
