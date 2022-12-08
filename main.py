import turtle as trtl

#for multi threading
from multiprocessing.pool import ThreadPool
import threading

#screen size
screen_h = 200
screen_w = 200

wn = trtl.Screen()
wn.setup(width=screen_w, height=screen_h)

wn.bgpic("ocean.gif") 

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
t3 = threading.Thread(target=elements_moves, args=("shark.gif", -100, -40, 1.5, "shark.gif", 0))
t3.setDaemon(True)
t3.start()
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

#fish_shapes = ["fish1.gif", "fish2.gif", "fish3.gif", "fish4.gif"]

#commands for fish movement

#----- init fish
'''for i in fish_shapes:
  wn.addshape(i)
  fish = trtl.Turtle(shape=i)
  fish.hideturtle()
  fish.penup()
  fish.setheading(0)
  fish.turtlesize(1.5, 1.5)
  fish.goto(0, 0)
  fish.speed(2)
  fish.showturtle()
  fish.forward(300)'''

#trtl.goto(100, 100)

wn.mainloop()
