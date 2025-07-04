name=input("enter your name here:")
age=int(input("enter your age here:"))
score=int(input("enter your 12th percentage  here:"))



if (age>20 and score>60):
    print("you are good to go")                                                   #greater#


elif(age>20 and score<60):
  print("youn are not eligable better luck next time !!!!!")


elif(age<20 and score>60):
  print("youn are not eligable better luck next time !!!!!")


else:
    print("not eligable sorry",name)