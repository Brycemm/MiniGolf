name = input("Welcome to GC Mini Golf! What is your name?")

A = input("Hi, " + name + ". Would you like to play 3 or 6 holes today?")


if A == "3":
    str1 = float(input("How many putts for hole 1? (par: 3)"))
    str2 = float(input("How many putts for hole 2? (par: 3)"))
    str3 = float(input("How many putts for hole 3? (par: 3)"))

    if A == "3":
        str4 = 3
        str5 = 3
        str6 = 3
else:
    str1 = float(input("How many putts for hole 1? (par: 3)"))
    str2 = float(input("How many putts for hole 2? (par: 3)"))
    str3 = float(input("How many putts for hole 3? (par: 3)"))
    str4 = float(input("How many putts for hole 4? (par: 3)"))
    str5 = float(input("How many putts for hole 5? (par: 3)"))
    str6 = float(input("How many putts for hole 6? (par: 3)"))

sum_putts = str1 + str2 + str3 + str4 + str5 + str6 - 18
par = sum_putts

if par == 0:
    print("Good game, " + name + ". Your total par was: 0")
elif par > 0:
    print("Nice try, " + name + "... Your total par was: +" + str(sum_putts) +"")
elif par < 0:
    print("Great job, " + name + "! Your total par was: " + str(sum_putts) +"")
