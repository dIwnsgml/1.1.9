import turtle as trtl


#for multi threading
import threading


import random


#rain part part of code
canvheight = 600
canvwidth = 800

wn = trtl.Screen()

wn.setup(canvwidth, canvheight)


p = trtl.Turtle()



p.penup()
p.goto(0,0)
p.forward(100)
p.left(90)
p.forward(100)
p.left(90)
p.forward(200)
p.left(90)
p.forward(200)
p.left(90)
p.forward(200)
p.left(90)
p.forward(100)
p.right(90)


#The code below is for the cloud
#This code is for the big circle part of the cloud.
p.pencolor("grey")
p.fillcolor("dark grey")
p.penup()
p.goto(-3,50)
p.pendown()
p.begin_fill()
p.circle(23)
p.end_fill()
p.goto(-3,50)
p.pensize(5)
p.pencolor("light grey")
p.circle(23,200)
p.pencolor("grey")
#Code below is for the second biggest circle in the cloud on the right
p.circle(23,185)
p.goto(27,51)
p.begin_fill()
p.circle(18)
p.end_fill()
p.goto(27,51)
p.pensize(5)
p.pencolor("light grey")
p.circle(18,190)
p.penup()
#code below is the second biggest circle for the cloud on the left.
p.goto(-38,83)
p.pendown()
p.pencolor("dark grey")
p.begin_fill()
p.circle(18)
p.end_fill()
p.circle(18,270)
p.pencolor("grey")
p.circle(18,275)
p.penup()
#Code below is the circle for the cloud on the far left.
p.goto(-42,51)
p.pendown()
p.pencolor("dark grey")
p.begin_fill()
p.circle(12)
p.end_fill()
p.circle(12,100)
p.pencolor("grey")
p.pensize(5)
p.circle(12,280)
p.penup()
#code below is for the medium sized circle for the cloud, before the farthest on the right. 
p.goto(57,55)
p.begin_fill()
p.circle(15)
p.end_fill()
p.pendown()
p.pencolor("light grey")
p.circle(15,185)
p.pencolor("dark grey")
p.circle(15,60)
p.pencolor("grey")
p.circle(15,105)
p.penup()
#Code below is for the small circle in the cloud, farthest to the right. 
p.goto(75,51)
p.pendown()
p.pencolor("dark grey")
p.begin_fill()
p.circle(12)
p.end_fill()
p.pencolor("light grey")
p.circle(12,185)
p.pencolor("dark grey")
p.circle(12,60)
p.pencolor("grey")
p.circle(12,105)
# Code below is for the lightning bolt.
p.penup()
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
p.setheading(360)

#this code for ocean
p.pensize(1)
p.begin_fill()
p.fillcolor("light blue")
p.penup()
p.goto(-100,0)
p.pendown()
p.pencolor("light blue")
for i in range(4):
  p.sety(0)
  p.setheading(0)
  p.pendown()
  p.circle(29,60)
  p.setheading(300)
  p.circle(29,60)
p.goto(100, -100)
p.goto(-100,-100)
p.goto(-100,0)
p.end_fill()

p.begin_fill()
p.fillcolor("#3B5387")
p.penup()
p.goto(-100,-25)
p.pendown()
p.pencolor("azure")
p.pensize(4)
for i in range(4):
  p.sety(-25)
  p.setheading(0)
  p.pendown()
  p.circle(29,60)
  p.setheading(300)
  p.circle(29,60)
p.goto(100, -100)
p.goto(-100,-100)
p.goto(-100,-25)
p.end_fill()

p.begin_fill()
p.fillcolor("#1F254A")
p.penup()
p.goto(-100,-50)
p.pendown()
p.pencolor("azure")
p.pensize(4)
for i in range(4):
  p.sety(-50)
  p.setheading(0)
  p.pendown()
  p.circle(29,60)
  p.setheading(300)
  p.circle(29,60)
p.goto(100, -100)
p.goto(-100,-100)
p.goto(-100,-50)
p.end_fill()

#this code for sand
p.pensize(1)
p.penup()
p.goto(-100,-90)
p.pendown()
p.begin_fill()
p.pencolor("black")
p.fillcolor("#ADAD8B")
p.setheading(30)
p.circle(-200,30)
p.circle(-200,30)
p.goto(100,-100)
p.goto(-100,-100)
p.goto(-100,-90)
p.end_fill()

#this code for seeweed
p.penup()
p.goto(-50,-85)
p.pendown()
p.begin_fill()
p.pencolor("black")
p.fillcolor("#1A5704")
p.setheading(53)
p.circle(15,70)
p.left(110)
p.circle(15,70)
p.penup()
p.goto(-50,-70)
p.pendown()
p.setheading(53)
p.circle(15,70)
p.left(110)
p.circle(15,70)
p.penup()
p.goto(-50,-55)
p.pendown()
p.setheading(53)
p.circle(15,70)
p.left(110)
p.circle(15,25)
p.end_fill()
#this code for seeweed(2)
p.penup()
p.goto(50,-90)
p.pendown()
p.begin_fill()
p.pencolor("black")
p.fillcolor("#1A5704")
p.setheading(53)
p.circle(20,70)
p.left(110)
p.circle(20,70)
p.penup()
p.goto(50,-70)
p.pendown()
p.setheading(53)
p.circle(20,70)
p.left(110)
p.circle(20,70)
p.penup()
p.goto(50,-50)
p.pendown()
p.setheading(53)
p.circle(20,70)
p.left(110)
p.circle(20,70)
p.end_fill()
#rock
p.penup()
p.goto(0,-95)
p.pendown()
p.pencolor('black')
p.fillcolor('darkgrey')
p.begin_fill()
p.setheading(0)
p.circle(10,360,5)
p.end_fill()






















#screen size
screen_h = 200
screen_w = 200

wn = trtl.Screen()
wn.setup(width=screen_w, height=screen_h)

#wn.bgpic("ocean.gif") 

def elements_moves(fish_shape1, x, y, fish_speed, fish_shape2, start_heading):
  fish_shapes = [fish_shape1, fish_shape2]
  shape_i = 0
  fish_direction = start_heading
  wn.addshape(fish_shapes[0])
  fish = trtl.Turtle(shape=fish_shapes[0])
  fish.hideturtle()
  fish.penup()
  fish.setheading(fish_direction)
  fish.turtlesize(1.5, 1.5)
  fish.goto(x, y)
  fish.speed(2)
  fish.showturtle()
  while(1):
    fish.forward(fish_speed)
    if(fish.xcor() > 100 and fish_direction == 0):
      shape_i += 1
      wn.addshape(fish_shapes[shape_i % 2])
      fish.shape(fish_shapes[shape_i % 2])
      fish_direction += 180
      fish.setheading(fish_direction)
    if(fish.xcor() < -100 and fish_direction == 180):
      shape_i += 1
      wn.addshape(fish_shapes[shape_i % 2])
      fish.shape(fish_shapes[shape_i % 2])
      fish_direction -= 180
      fish.setheading(fish_direction)



'''thr = [0, 0]
thr[0] = threading.Thread(target = fish1_moves) #args = (x)
thr[1] = threading.Thread(target = fish2_moves)

thr[0].start()
thr[1].start()

thr[0].join()
thr[1].join()'''
t1 = threading.Thread(target=elements_moves, args=("fish1.gif", -100, -40, 1.5, "fish1-1.gif", 0))
t1.setDaemon(True)
t1.start()
t1 = threading.Thread(target=elements_moves, args=("fish3.gif", 100, -60, 3, "fish3-1.gif", 180))
t1.setDaemon(True)
t1.start()
t2 = threading.Thread(target=elements_moves, args=("fish4.gif", 100, -70, 2, "fish4-1.gif", 180))
t2.setDaemon(True)
t2.start()
'''t3 = threading.Thread(target=elements_moves, args=("shark.gif", -100, -40, 1.5, "shark.gif", 0))
t3.setDaemon(True)
t3.start()'''
'''fish_n = 3
threads = [0,0,0,0]
fish_shape1 = ["fish1.gif","fish2.gif","fish3.gif","fish4.gif"]
fish_shape2 = ["fish1-1.gif","fish2-1.gif","fish3-1.gif","fish4-1.gif"]
fish_speed = [1.5, 2, 1, 0.7]
fish_cor = [[-100, -40], [100, -30], [100, -50], [-100, -30]]
fish_dir = [180, 0, 0, 0]
for i in range(fish_n):
  threads[i] = threading.Thread(target=elements_moves, args=(fish_shape1[i], fish_cor[i[0]], fish_cor[i[1]], fish_speed[i], fish_shape2[i], fish_dir[i]))
  threads[i].setDaemon(True)
  threads[i].start()'''




















#rain part of code starts here
#Flashs are also here
p.color("black")
def rain():
  horiz_turtles = []
  


# use interesting shapes and colors
  trtl.color("black")

  turtle_shapes = ["circle", "circle", "circle", "circle", "circle", "circle", "circle", "circle", "circle", "circle", "circle", "circle"] 
  trtl.color("black")
  tloc = -50
  p.shapesize(0.01)
  for s in turtle_shapes:
  #The code will run until it uses each element in turrtle shape 
    trtl.hideturtle()
    trtl.color("black")
    
    ht = trtl.Turtle(shape=s)
    ht.turtlesize(200)
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
    ht.shapesize(0.5)
    ht.color("black")
    ht.speed(10000000000000000000000000000000000000)
    ht.color("black")
    ht.pensize(0.5)
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
    ht.turtlesize(0.5)
    ht.color("black")
    ht.goto(tloc, 60)
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
    tloc += 10
 
  # TODO: move turtles across and down screen,creating the drop lets
  for step in range(4):
    for ht in horiz_turtles:
      roll = random.randint(1,10)
      second_roll = random.randint(1,10)
      ht.pendown()
      ht.forward(roll)
      ht.penup()
      ht.forward(second_roll)
      ht.hideturtle()
      
      ht.shapesize(0.000001)

      ht.clear()
      
     

    










t4 = threading.Thread(target=rain)
t4.setDaemon(True)
t4.start()
wn = trtl.Screen()
wn.mainloop()