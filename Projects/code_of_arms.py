# Section 1 - Your code
from utils import *
set_background("Oceann.gif")

s5 = create_sprite("White_Box.gif", 0, 0)
s1 = create_sprite("Italy.gif", 50, 50)
s2 = create_sprite("dog", -150, 50)
s3 = create_sprite("volleyball.gif", -100, -100)
s4 = create_sprite("cardinal", 100, -100)

message1 = create_sprite("alien",-250,230)
message1.color("blue")
message1.write("Corinna",font = ("Arial", 40, "normal"))
message1.hideturtle()

message2 = create_sprite("alien",-250,-280)
message2.color("blue")
message2.write("dogs are the best",font = ("Arial", 40, "normal"))
message2.hideturtle()


######################################################################


# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()