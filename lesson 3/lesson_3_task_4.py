from turtle import *

t = Turtle()
t.speed(0)
t.screen.setup(800, 800)
t.screen.bgcolor("yellow")

def draw_circle(color, radius, x, y):
     t.penup()
     t.goto(x, y)
     t.pendown()
     t.color(color)
     t.begin_fill()
     t.circle(radius)
     t.end_fill()

def draw_triangle(color, size):
    t.color(color)
    t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    t.end_fill()

def draw_line(color, x, y, length):
    t.color(color)
    t.penup()
    t.goto(x, y)
    t.pendown()
    angles = [-30, 0, 30]
    for angle in angles:
        t.setheading(angle + 180)
        t.forward(length)
        t.penup()
        t.goto(x, y)
        t.pendown()

    for angle in angles:
        t.setheading(angle) 
        t.forward(length)
        t.penup()
        t.goto(x, y)
        t.pendown()

# Голова кота
draw_circle("gray", 110, 0, 0)

# Уши кота
t.penup()
t.goto(65, 200)
t.pendown()
t.color("grey")
t.begin_fill()
t.left(45)
t.forward(80)
t.right(145)
t.forward(110)
t.end_fill()


t.penup()
t.goto(-65, 200)
t.pendown()
t.color("grey")
t.begin_fill()
t.right(125)
t.forward(80)
t.left(145)
t.forward(110)
t.end_fill()


t.penup()
t.goto(100, 210)  
t.pendown()
t.setheading(210)  
draw_triangle("pink", 30)

t.penup()
t.goto(-100, 180)  
t.pendown()
t.setheading(35)  
draw_triangle("pink", 30)

# Глаза кота
draw_circle("white", 25, -30, 140)
draw_circle("white", 25, 50, 140)

draw_circle("blue", 10, -40, 150)
draw_circle("blue", 10, 40, 150)


# Рот кота
t.penup()
t.goto(0, 60)
t.pendown()
t.color("pink")
t.right(120)
t.circle(10, 180)
t.penup()
t.goto(0, 60)
t.pendown()
t.circle(10, -180)

# Усы кота
draw_line("black", 0, 100, 150)

# Нос кота
draw_circle("pink", 15, 5, 90)

t.hideturtle()
t.screen.exitonclick()
t.screen.mainloop()
