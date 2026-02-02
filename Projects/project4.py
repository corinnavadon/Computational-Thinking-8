import turtle, time, random
from utils import *

#the goal of the game is to get cupcakes to sell for money and with the money buy chefs

set_background("bakery")


Cupcakes = 0
Chefs = 0
Money = 0

message_sprite = create_sprite("alien", -200,200)
message_sprite.hideturtle()

def make_cupcake():
    global Cupcakes
    Cupcakes += 1
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    c1 = create_sprite("Cupcake", x, y)
    time.sleep(0.1)
    c1.hideturtle()

window.onkeypress(make_cupcake, "space")
#this key increases the amount of cupcakes there is 

def get_chef():
    global Money, Chefs 
    if Money >= 100:
       Chefs += 1
       Money -= 100

       x = random.randint(-200,200)
       y = -250
       create_sprite("chef",x,y)
       
       
window.onkeypress(get_chef, "c")
# this key allows you to buy a chef once you have enough money


def get_money():
    global Money, Cupcakes
    if Cupcakes >= 50:
        Money += 100 
        Cupcakes -= 50
        
        
        
window.onkeypress(get_money, "m")
# this key turns 50 cupcakes into 100 money
        
window.listen()
for i in range(1000000000):
    if Chefs == 1:
        time.sleep(1)
        Cupcakes += 1
    elif Chefs == 2:
        time.sleep(1)
        Cupcakes += 2
    elif Chefs == 3:
        time.sleep(1)
        Cupcakes += 3
    elif Chefs == 4:
        time.sleep (1)
        Cupcakes += 4
    elif Chefs == 5:
        time.sleep (1)
        Cupcakes += 5
    elif Chefs == 6:
        time.sleep (1)
        Cupcakes += 6
    elif Chefs == 7:
        time.sleep (1)
        Cupcakes += 7
    elif Chefs >= 8:
        time.sleep (1)
        Cupcakes += 8
    #these make the cupcakes increase automatically based on how many chefs there is 

    message_sprite.clear()
    message_sprite.write(f"Cupcakes: {Cupcakes}\nMoney: {Money}\nChefs: {Chefs}", font=("Arial",15,"normal"))

    time.sleep(0.01)
    window.update()