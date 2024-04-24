import math
name = input("Welcome to GC mini golf! What is your name?:")
number_hole = input("Hi," +name+ "! Would you like to play 3 or 6 holes today?")
if number_hole == "3":
    hole1 = input("How many putts for hole 1? (par:3)?")
    hole2 = input("How many putts for hole 2? (par:3)?")
    hole3 = input("How many putts for hole 3? (par:3)?")
    par9 = int(hole1) + int(hole2) + int(hole3)
    if par9 >9:
        print("Nice try," + name +". Your total score was:+" +str(par9) + ".")
    elif par9 <9:
        print("Great job," + name + "! Your total score was:-" +str(par9) + ".")
    elif par9 ==9:
        print("Good game," + name+ ". Your total score was:" +str(0) + ".")
if number_hole == "6":
    hole_1 = input("How many putts for hole 1? (par:3)?")
    hole_2 = input("How many putts for hole 2? (par:3)?")
    hole_3 = input("How many putts for hole 3? (par:3)?")
    hole_4 = input("How many putts for hole 4? (par:3)?")
    hole_5 = input("How many putts for hole 5? (par:3)?")
    hole_6 = input("How many putts for hole 6? (par:3)?")
    par18 = int(hole_1) + int(hole_2) + int(hole_3) + int(hole_4) + int(hole_5) + int(hole_6)
    if par18 > 18:
        print("Nice try," + name +". Your total score was:+" +str(par18) + ".")
    elif par18 < 18:
        print("Great job," + name + "! Your total score was:-" +str(par18) + ".")
    elif par18 == 18:
        print("Good game," + name+ ". Your total score was:" +str(0) + ".")