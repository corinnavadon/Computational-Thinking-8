import turtle, time, random
from utils import *

x1 = -280
y1 = 70
x2 = -280
y2 = -70
x3 = -280
y3 = 200
x4 = -280
y4 = -200


set_background("field.gif")
t1 = create_sprite("dog1.gif",x1,y1)
t2 = create_sprite("dog2.gif",x2,y2)
t3 = create_sprite("dog3.gif",x3,y3)
t4 = create_sprite("dog4.gif",x4,y4)


for i in range(50):
    x1 += random.randint(7,12) 
    # x1 is first dog can be okay or pretty slow
    x2 += random.randint(10,14) 
    # x2 is second dog and is like medium speed
    x3 += random.randint(3,22)
    # x3 is third dog and can be really fast or really slow
    x4 += random.randint(6,18)
    # x4 is last dog can be pretty fast or pretty slow

    t1.goto(x1, y1)
    t2.goto(x2, y2)
    t3.goto(x3, y3)
    t4.goto(x4, y4)

    window.update()
    time.sleep(0.1)

print(" ")

if x2 >= x1 and x2 >= x3 and x1 >= x4:
    print("player 2 wins!")
elif x1 >= x2 and x1 >= x3 and x1 >= x4:
    print("player 1 wins!")
elif x3 >= x1 and x3 >= x2 and x3 >= x4:
    print("player 3 wins!")
elif x4 >= x1 and x4 >= x2 and x4 >= x3:
    print("player 4 wins!")
