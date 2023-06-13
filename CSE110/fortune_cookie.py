if __name__ == '__main__':

    print("Welcome to Zach's Virtual Fortune Cookie Jar")
    asking = True
    while asking:
        print("There are 10 different colored fortune cookies.")
        print("-"*20)
        print("Cookies: Red, yellow, blue, orange, green, purple, pink, white, brown, black.")
        print("-"*20)
        cookie = input("Enter a color to pick one (no caps).")
        asking = False

    if cookie == "red":
        print("")
        print("-"*20)
        print("You are about to eat a stale cookie. -Jim Gaffigan")
        print("-"*20)

    elif cookie == "green":
        print("")
        print("-"*20)
        print("Tomorrow you will play a game of phone tag with someone from the DMV.")
        print("-"*20)
    
    elif cookie == "yellow":
        print("")
        print("-"*20)
        print("Next week, you will slip a peel,\n but not a banana peel.")
        print("-"*20)
    
    elif cookie == "purple":
        print("")
        print("-"*20)
        print("Ask again later.")
        print("-"*20)

    elif cookie == "orange":
        print("")
        print("-"*20)
        print("Sorry [USER], but your fortune is in another cookie.")
        print("-"*20)
    
    elif cookie == "blue":
        print("")
        print("-"*20)
        print("You will eat a piece of toast with nutella and peanut butter on it.\nIt will be delicous.")
        print("-"*20)
    
    elif cookie == "pink":
        print("")
        print("-"*20)
        print("On this Friday you will see a toddler trip in public.\nYou should probably help him up.")
        print("-"*20)
    
    elif cookie == "white":
        print("")
        print("-"*20)
        print("Three days from now a magpie will try to steal your car keys.\nI reccomend buying some magpie deterrent.")
        print("-"*20)
    
    elif cookie == "brown":
        print("")
        print("-"*20)
        print("You will play Root by Leder Games next week.\nIt is Zach's favourite boardgame.\nHe higly reccommends it.")
        print("-"*20)
    
    elif cookie == "black":
        print("")
        print("-"*20)
        print("What do you think this is some stinkin' fortune cookie buffet?\nOh it is? Never mind.\nYou will eat a cookie tomorrow.")
        print("-"*20)

    else:
        print("")
        print("That is not a cookie.")