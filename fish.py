import turtle as trtl
wn = trtl.Screen()

def create_fish(fish_shape1, x, y, fish_speed, fish_shape2, start_heading):
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
    if(fish.xcor() > 400 and fish_direction == 0):
      shape_i += 1
      wn.addshape(fish_shapes[shape_i % 2])
      fish.shape(fish_shapes[shape_i % 2])
      fish_direction += 180
      fish.setheading(fish_direction)
    if(fish.xcor() < -400 and fish_direction == 180):
      shape_i += 1
      wn.addshape(fish_shapes[shape_i % 2])
      fish.shape(fish_shapes[shape_i % 2])
      fish_direction -= 180
      fish.setheading(fish_direction)