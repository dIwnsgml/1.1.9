import turtle as trtl
import random

p = trtl.Turtle()
p.speed(10000000)


def create_lightening():
  while (True):
    p.pencolor("yellow")
    x = random.randrange(-400, 400)
    for i in range(3):
      p.penup()
      p.goto(x, 230)
      p.pendown()
      for i in range(10):
        p.pensize(10 - i)
        p.setheading(random.randrange(240, 300))
        p.forward(i * 6)
    p.clear()


'''  p.penup()
  p.goto(15,47)
  p.pendown()
  p.pensize(4)

  colors = ["red", "orange", "yellow"]

  color = random.choice(colors)
  p.fillcolor(color)
  p.begin_fill()
  p.right(65)
  color = random.choice(colors)
  p.pencolor(color)
  p.circle(18,70)
  p.right(110)
  p.circle(12,20)
  p.right(65)
  p.forward(18)
  p.left(110)
  p.forward(10)
  p.right(110)
  p.forward(30)
  p.right(155)
  p.forward(20)
  p.left(85)
  p.forward(8)
  p.right(100)
  p.forward(25)
  p.end_fill()
  p.penup()
  p.goto(15,48)
  p.pendown()
  p.pensize(6)
  p.right(89)
  p.pencolor("grey")
  p.circle(18,52)
  p.penup()
  p.goto(20,0)
  p.pendown()
  p.setheading(360)'''

p.color("black")


def rai_n():
  while True:

    horiz_turtles = []

    # use interesting shapes and colors
    trtl.color("black")

    turtle_shapes = ["circle", "circle", "circle", "circle", "circle", "circle", "circle", "circle", "circle", "circle", "circle", "circle", "circle", "circle", "circle", "circle", "circle", "circle"]
    trtl.color("black")
    tloc = -400
    p.shapesize(0.01)
    for s in turtle_shapes:
      print("aaa")
      #The code will run until it uses each element in turrtle shape
      trtl.hideturtle()
      trtl.color("black")

      ht = trtl.Turtle(shape=s)
      ht.turtlesize(600)
      ht.color("black")
      ht.hideturtle()
      ht.color("black")

      ht.speed(10)
      ht.color("black")
      ht.color("black")
      ht.pencolor("darkblue")
      ht.speed(10000000000000000000000000000000000000)
      ht.color("lightblue")
      horiz_turtles.append(ht)
      ht.color("black")
      ht.speed(10)
      ht.color("black")
      ht.shapesize(0.55)
      ht.color("black")
      ht.speed(10000000000000000000000000000000000000)
      ht.color("black")
      ht.pensize(3)
      ht.color("black")
      ht.speed(10000000000000000000000000000000000)
      ht.color("black")
      ht.penup()
      ht.color("black")
      ht.shapesize()
      ht.color("black")
      ht.speed(1000000000000000000000000000000000000000000)
      ht.color("black")
      ht.fillcolor("black")
      ht.color("black")
      ht.speed(10)
      ht.color("black")
      ht.color("black")
      ht.color("black")
      ht.turtlesize(5)
      ht.color("black")
      ht.goto(tloc, 250)
      ht.color("black")
      ht.shapesize(0.5)
      ht.color("black")
      ht.speed(10000000000000000000000000000000000000)
      ht.color("black")
      ht.setheading(270)
      ht.pencolor("darkblue")
      ht.hideturtle()

      # this code sets up the shape before it moves
      #This part of the code adds the direction to the set up shapes
      tloc += 50

    # TODO: move turtles across and down screen,creating the drop lets
    for step in range(7):
      for ht in horiz_turtles:
        roll = random.randint(1, 10)
        second_roll = random.randint(1, 10)
        ht.pendown()
        ht.forward(roll)
        ht.penup()
        ht.forward(second_roll)
        ht.hideturtle()

        ht.shapesize(0.000001)

        ht.clear()
        