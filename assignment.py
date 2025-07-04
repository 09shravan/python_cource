print(" !!! welcome in kon banega corerpati show !!! ")

print("the first question is for $2000 \n")

str(input("type READY! to start the game : "))

print("Which planet is the largest in the solar system...\n")



a=print("option (a) earth")
b=print("option (b) mars")
c=print("option (c) saturn")
d=print("option (d) jupiter")

answer=str(input("enter your answer here:"))

if answer.lower() == "d" or answer.lower() == "jupiter":
    print("you won 2000$")


else:
    print("you loose the game")
    exit()

print("the second question is for $5000 \n")

print("Which is largest continent in the world...\n")

a=print("option (a) africa")
b=print("option (b) asia")
c=print("option (c) europe")
d=print("option (d) austrialia")

answer=str(input("enter your answer here:"))

if answer.lower() == "b" or answer.lower() == "asia":
    print("you won 5000$")


else:
    print("you loose the game")
    exit()


print("the third question is for $5000 \n")

print("what is the currency of japan...\n")

a = print("option (a) dollar")
b = print("option (b) won")
c = print("option (c) yen")
d = print("option (d) peso")

answer = str(input("enter your answer here:"))

if answer.lower() == "c" or answer.lower() == "yen":
    print("you won 7000$")


else:
    print("you loose the game")
    exit()

print("the forth question is for $8000 \n")

print("Which  Which is the largest ocean in the world?...\n")

a = print("option (a) Indian Ocean")
b = print("option (b)  Atlantic Ocean")
c = print("option (c) Arctic Ocean")
d = print("option (d) Pacific Ocean ")

answer = str(input("enter your answer here:"))

if answer.lower() == "d" or answer.lower() == "pacific ocean":
   print("you won 10000$")

else:
    print("you loose the game")
    exit()

print("!!congralutions!! you won the game total amount you won is 24000$")