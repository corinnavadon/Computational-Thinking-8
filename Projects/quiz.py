dog_points = 0
cat_point = 0
hamster_points = 0
fish_points = 0
rabbit_point = 0 

print("----------------------------------------------------------")
print(" ")
print("for this game make sure to answer in letters that are capital with no spaces. and make sure to press enter 2 times between questions")
print(" ")
print("----------------------------------------------------------")
print(" ")

answer1 = input("do you like A bigger animals or B small animals? ")
if answer1 == "A":
    dog_points += 1
    cat_point += 1
elif answer1 == "B":
    hamster_points += 1
    fish_points += 1
elif answer1 == "A" or  answer1 == "B":
    rabbit_point += 1

input(" ")

Answer2 = input("do you have a lot of room in your house? A Yes a lot B No not at all, or C a bit of room? ")
if Answer2 == "A":
    dog_points += 1
    cat_point += 1 
elif Answer2 == "B":
    fish_points += 1
    hamster_points += 1
elif Answer2 == "C": 
    rabbit_point += 1
    hamster_points += 1

input(" ")

Answer3 = input("do you have experience in having pets? A yes B no C a bit? ")
if Answer3 == "A":
    dog_points += 1
    cat_point += 1
elif Answer3 == "B":
    fish_points += 1
elif Answer3 == "C":
    hamster_points += 1
    rabbit_point += 1

input(" ")

Answer4 = input("do you have a lot of time to care for pets? A yes! B no much C a bit? ")
if Answer4 == "A":
    dog_points += 1
elif Answer4 == "B":
    fish_points += 1
    hamster_points +=1
elif Answer4 == "C":
    rabbit_point += 1 
elif Answer4 == "A" or Answer4 == "C":
    cat_point += 1


input(" ")

Answer5 = input("which pet do you like the most? A dogs B cats C hamsters D rabbits or E fish? ")
if Answer5 == "A":
    dog_points += 1
elif Answer5 == "B":
    cat_point += 1
elif Answer5 == "C":
    hamster_points += 1
elif Answer5 == "D":
    rabbit_point += 1
elif Answer5 == "E":
    fish_points += 1

input(" ")

Answer6 = input("Are you prepared for a pet with a long lifetime? A yes B no? ")
if Answer5 == "A":
    dog_points += 1
    cat_point += 1
    rabbit_point += 1
elif Answer5 == "B":
    fish_points += 1
    hamster_points += 1

input(" ")

Answer7 = input("are you willing to spend money on things like medical, and others. A yes B no? ")
if Answer7 == "A":
    cat_point += 1
    dog_points += 1
    rabbit_point += 1
elif Answer7 == "B":
    fish_points += 1
    hamster_points += 1

input("")
print(" ")
print("-----------------------------------------------")
print(" ")

if dog_points > cat_point and dog_points > rabbit_point and dog_points > hamster_points and dog_points > fish_points:
    print("You should get a dog. The dog requirements match with your own!")
    print("dogs are kind usually bigger animals who need lots of attention and space")

elif cat_point > dog_points and cat_point > rabbit_point and cat_point > hamster_points and cat_point > fish_points:
    print("you should get a cat, the cat requirements match your own!")
    print("cats are smaller cute and kind animals who need a medium amount of attention")    

elif rabbit_point > dog_points and rabbit_point > cat_point and rabbit_point > hamster_points and rabbit_point > fish_points:
    print("you should get a rabbit! rabbit requirements match your own!")
    print("rabbits are small fluffy animals who need minimal room and attention")

elif hamster_points > dog_points and hamster_points > cat_point and rabbit_point > fish_points and hamster_points > rabbit_point:
    print("you should get a hamster! the hamster requirements match your own")
    print("hamsters and small fluffy animals who need minimal attention and not too much room")

elif fish_points > dog_points and fish_points > cat_point and fish_points > hamster_points and fish_points > rabbit_point:
    print("you should get a fish. the fish requirements match your own")
    print("fish are tiny weird little things who need no attention and just swim around")

else:
    print("Its a tie! you matched multiple animals you can choose!")

print(" ")
print("------------------------------------------------")