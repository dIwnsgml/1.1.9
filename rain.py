import random
import turtle as trtl

def rai_n():
  while True:
    x = random.randint(-400, 400)
    y = random.randint(20, 300)
    horiz_turtles = []

    # use interesting shapes and colors
    trtl.color("black")

    turtle_shapes = ["circle", "circle", "circle", "circle", "circle", "circle", "circle", "circle", "circle", "circle", "circle", "circle", "circle", "circle", "circle", "circle", "circle", "circle"]
    trtl.color("black")
    tloc = -200
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
        