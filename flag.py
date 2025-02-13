import turtle

flag = turtle.Turtle()
flag.speed(3)
turtle.bgcolor("black")
flag.pencolor("pink")
flag.shape("turtle")
turtle.title("Philippine Flag")

flag.penup()
flag.goto(-300,100)
flag.pendown()
flag.begin_fill()
flag.color("blue")
flag.fd(600)
flag.rt(90)
flag.fd(150)
flag.rt(90)
flag.fd(600)
flag.rt(90)
flag.fd(150)
flag.end_fill() #rectangle

flag.penup()
flag.goto(-300,-50)
flag.pendown()
flag.begin_fill()
flag.color("red")
flag.lt(270)
flag.fd(600)
flag.rt(90)
flag.fd(150)
flag.rt(90)
flag.fd(600)
flag.rt(90)
flag.fd(150)
flag.end_fill()#rectangle

flag.penup()
flag.goto(-40,-50)
flag.pendown()
flag.begin_fill()
flag.color("white")
flag.circle(173, steps=3) #triangle
flag.end_fill()

flag.penup()
flag.goto(-270,20)
flag.pendown()
flag.begin_fill()
flag.color("yellow")
flag.pensize(3)
flag.fd(50)
flag.rt(144)
flag.fd(50)
flag.rt(144)
flag.fd(50)
flag.rt(144)
flag.fd(50)
flag.rt(144)
flag.fd(50)
flag.rt(144) #star
flag.end_fill()

flag.penup()
flag.goto(-130,-77)
flag.pendown()
flag.begin_fill()
flag.color("yellow")
flag.pensize(3)
flag.fd(50)
flag.rt(144)
flag.fd(50)
flag.rt(144)
flag.fd(50)
flag.rt(144)
flag.fd(50)
flag.rt(144)
flag.fd(50)
flag.rt(144) #star
flag.end_fill()

flag.penup()
flag.goto(-270,-160)
flag.pendown()
flag.begin_fill()
flag.color("yellow")
flag.pensize(3)
flag.fd(50)
flag.rt(144)
flag.fd(50)
flag.rt(144)
flag.fd(50)
flag.rt(144)
flag.fd(50)
flag.rt(144)
flag.fd(50)
flag.rt(144) #star
flag.end_fill()

flag.penup()
flag.goto(-230, -50)
flag.pendown()
flag.color("yellow")
flag.pensize(6)
flag.fd(50)
flag.bk(50)
flag.rt(30)
flag.fd(50)
flag.bk(50)
flag.rt(30)
flag.fd(50)
flag.bk(50)
flag.rt(30)
flag.fd(50)
flag.bk(50)
flag.rt(30)
flag.fd(50)
flag.bk(50)
flag.rt(30)
flag.fd(50)
flag.bk(50)
flag.rt(30)
flag.fd(50)
flag.bk(50)
flag.rt(30)
flag.fd(50)
flag.bk(50)
flag.rt(30)
flag.fd(50)
flag.bk(50)
flag.rt(30)
flag.fd(50)
flag.bk(50)
flag.rt(30)
flag.fd(50)
flag.bk(50)
flag.rt(30)
flag.fd(50)
flag.bk(50)
flag.rt(30) #sun
flag.end_fill()



flag.hideturtle()
turtle.done()
