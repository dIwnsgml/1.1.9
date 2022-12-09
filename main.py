import turtle as trtl
#for multi threading
import threading
import random
import keyboard

from cloud import create_clouds
from lightening import create_lightening
from ocean import create_ocean
from fish import create_fish

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
for i in range(7):
  cloud_x = random.randrange(-350, 350)
  cloud_y = random.randrange(200, 250)
  print(cloud_x, cloud_y)
  create_clouds(cloud_x, cloud_y)
# Code below is for the lightning bolt.

#this code for ocean
create_ocean()



wn.addshape("shark.gif")
shark = trtl.Turtle(shape = "shark.gif")
def controller():
  shark.forward(10)
'''wn.onkeypress(controller, "Left")
wn.listen()'''

'''thr = [0, 0]
thr[0] = threading.Thread(target = fish1_moves) #args = (x)
thr[1] = threading.Thread(target = fish2_moves)

thr[0].start()
thr[1].start()

thr[0].join()
thr[1].join()'''
fish_n = 0
t = [0,0,0,0,0]
fish_shape1 = ["fish1.gif","fish2.gif","fish3.gif","fish4.gif"]
fish_shape2 = ["fish1-1.gif","fish2-1.gif","fish3-1.gif","fish4-1.gif"]
fish_speed = [1.5, 2, 1, 0.7]
fish_cor = [[-100, -40], [100, -30], [100, -50], [-100, -30]]
fish_dir = [180, 0, 0, 0]


t[1] = threading.Thread(target=create_fish, args=("fish1.gif", -100, -40, 1.5, "fish1-1.gif", 0))
t[1].start()

t[3] = threading.Thread(target=create_lightening)
t[3].start()
'''while True:
  if(fish_n < 3):
    for i in range(3):
      t[i] = threading.Thread(target=create_fish, args=("fish1.gif", -100, -40, 1.5, "fish1-1.gif", 0))
      fish_n += 1
      t[i].start()
      fish_n = 6'''
'''for i in range(1):
  t1 = threading.Thread(target=elements_moves, args=("fish1.gif", -100, -40, 1.5, "fish1-1.gif", 0))
  t1.setDaemon(True)
  t1.start()
  t1 = threading.Thread(target=elements_moves, args=("fish3.gif", 100, -60, 3, "fish3-1.gif", 180))
  t1.setDaemon(True)
  t1.start()
  t2 = threading.Thread(target=elements_moves, args=("fish4.gif", 100, -70, 2, "fish4-1.gif", 180))
  t2.setDaemon(True)
  t2.start()'''
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








'''while True:
  if keyboard.is_pressed("up"):
    shark.forward(100)'''










#rain part of code starts here
#Flashs are also here

wn = trtl.Screen()
wn.mainloop()