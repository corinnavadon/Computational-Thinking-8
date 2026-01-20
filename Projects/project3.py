import turtle, time, random
from utils import *

# Section 1 - Variables
# TODO - add starting values for all the variables
x1 = -280
y1 = 70
x2 = -280
y2 = -70
x3 = -280
y3 = 200
x4 = -280
y4 = -200


# Section 2 - Setup
# # TODO - use your own background, and set your four turtles to images of your choice
set_background("field.gif")
t1 = create_sprite("dog1.gif",x1,y1)
t2 = create_sprite("dog2.gif",x2,y2)
t3 = create_sprite("dog3.gif",x3,y3)
t4 = create_sprite("basketball",x4,y4)


# # Section 3 - Racing
# # TODO - set how much each variable changes by and increase the number of repeats to at least 30
# # TODO - explain here which sprites are faster or slower
# for i in range(3):
#     x1 +=
#     x2 +=
#     x3 +=
#     x4 +=

#     t1.goto(x1, y1)
#     t2.goto(x2, y2)
#     t3.goto(x3, y3)
#     t4.goto(x4, y4)

#     window.update()
#     time.sleep(0.1)


# # Section 4 - Winner
# # TODO - complete the elif for player 2 winning
# # TODO - write another elif for player 3 and player 4
# if x1 >= x2 and x1 >= x3 and x1 >= x4:
#     print("player 1 wins!")
# elif
#     print("player 2 wins!")


turtle.exitonclick()