import turtle as trtl
#for multi threading
import threading
import random

from cloud import create_clouds
from lightening import create_lightening
from ocean import create_ocean

canvheight = 600
canvwidth = 800

wn = trtl.Screen()
wn.setup(canvwidth, canvheight)


p = trtl.Turtle()
#improve speed
p.speed(1000)
#for canvas layout
p.penup()
p.goto(0,0)
p.forward(400)
p.pendown()
p.left(90)
p.forward(300)
p.left(90)
p.forward(800)
p.left(90)
p.forward(600)
p.left(90)
p.forward(800)
p.left(90)
p.forward(300)
p.right(90)


#The code below is for the cloud
#This code is for the big circle part of the cloud.
for i in range(10):
  cloud_x = random.randrange(-350, 350)
  cloud_y = random.randrange(200, 250)
  print(cloud_x, cloud_y)
  create_clouds(cloud_x, cloud_y)
# Code below is for the lightning bolt.

#this code for ocean
create_ocean()
for i in range(10):
  create_lightening(random.randrange(-400, 400), 230)



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
      
     

    










'''t4 = threading.Thread(target=rain)
t4.setDaemon(True)
t4.start()'''
wn = trtl.Screen()
wn.mainloop()