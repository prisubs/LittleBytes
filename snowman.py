import turtle

# set the background color for the page
bg = turtle.Screen()
bg.bgcolor("dark blue")

# make a function to draw the circles
def draw_circle(turtle, color, size, x, y):
  turtle.penup()
  turtle.color(color)
  turtle.fillcolor(color)
  turtle.goto(x,y)
  turtle.pendown()
  turtle.begin_fill()
  turtle.circle(size)
  turtle.end_fill()
  
# start of main body for the program
tommy = turtle.Turtle()
tommy.shape("turtle")
tommy.speed(10)

draw_circle(tommy, "red", 20, 0, -40)
draw_circle(tommy, "white", 30, 0, -100)
draw_circle(tommy, "red", 50, 0, -200)

#make buttons
draw_circle(tommy, "#000000", 2, 0, -55)
draw_circle(tommy, "#000000", 2, 0, -65)
draw_circle(tommy, "#000000", 2, 0, -75)

#make arms
tommy.penup()
tommy.goto(-10,-45)
tommy.pendown()
tommy.pensize(5)
tommy.color("white")
tommy.goto(-75, -55)

tommy.penup()
tommy.goto(10,-45)
tommy.pendown()
tommy.pensize(5)
tommy.color("white")
tommy.goto(75, -55)

# draw the hat
tommy.penup()
tommy.goto(-35, -5,)
tommy.color("black")
tommy.pensize(6)
tommy.pendown()
tommy.goto(35,-5)

tommy.goto(-35,-5)
tommy.fillcolor("black")
tommy.color("black")
tommy.pensize(6)
tommy.pendown()
tommy.begin_fill()
tommy.goto(20,-5)
tommy.left(90)
tommy.forward(20)
tommy.left(90)
tommy.forward(40)
tommy.left(90)
tommy.forward(20)
tommy.end_fill()
