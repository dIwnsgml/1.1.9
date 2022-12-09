import turtle as trtl
import random
p = trtl.Turtle()
p.speed(1000)

def create_lightening(x, y):
  p.pencolor("yellow")
  for i in range(3):
    p.penup()
    p.goto(x, y)
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