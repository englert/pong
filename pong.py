import turtle

# Ablak

wn =turtle.Screen()
wn.setup(width=800, height=600)
wn.bgcolor('black')
wn.title('PONG')
wn.tracer(0)

# Bal ütő

bal = turtle.Turtle()
bal.speed(0)          # maximális sebesség: 0
bal.shape('square')   # négyszög alak
bal.shapesize(stretch_len=1,stretch_wid=5 )
bal.color('green')
bal.penup()
bal.goto(-350,0)

# Jobb ütő

jobb = turtle.Turtle()
jobb.speed(0)          # maximális sebesség: 0
jobb.shape('square')   # négyszög alak
jobb.shapesize(stretch_len=1,stretch_wid=5 )
jobb.color('red')
jobb.penup()
jobb.goto(350,0)


# Labda

labda = turtle.Turtle()
labda.speed(0)
labda.shape('circle')
labda.color('yellow')
labda.penup()
labda.goto(0,0)
labda.dx = 1
labda.dy = 1

def bal_fel():
    y = bal.ycor()
    y += 30
    bal.sety(y)
    
def bal_le():
    y = bal.ycor()
    y -= 30
    bal.sety(y)
    
def jobb_fel():
    y = jobb.ycor()
    y += 30
    jobb.sety(y)
    
def jobb_le():
    y = jobb.ycor()
    y -= 30
    jobb.sety(y)
    
wn.onkey(bal_fel, "w")
wn.onkey(bal_le, "s")
wn.onkey(jobb_fel, "o")
wn.onkey(jobb_le, "l")

wn.listen()

while True:
    # a képernyő frissítése
    wn.update()
    
    labda.setx(labda.xcor() + labda.dx)
    labda.sety(labda.ycor() + labda.dy)
    
    # tetejéről pattanjon vissza
    if labda.ycor() > 288:
        labda.sety(288)
        labda.dy *= -1

    # aljáról pattanjon vissza
    if labda.ycor() < -288:
        labda.sety(-288)
        labda.dy *= -1
        
    # jobb oldal érintése
    if labda.xcor() >388:
        labda.goto(0,0)
        labda.dx *= -1
    # bal oldal érintése
    if labda.xcor() < -388:
        labda.goto(0,0)
        labda.dx *= -1
    #jobb ütő    
    lx,ly,jx,jy = labda.xcor(), labda.ycor(), jobb.xcor(), jobb.ycor()
    if jx-20 < lx < jx and jy-40 < ly < jy +40:
        labda.setx(jx-20)
        labda.dx *=-1
    #bal ütő    
    lx,ly,bx,by = labda.xcor(), labda.ycor(), bal.xcor(), bal.ycor()
    if bx+20 > lx > bx and by-40 < ly < by +40:
        labda.setx(bx+20)
        labda.dx *=-1    
    
        