choice_1 = False
choice_2A = False
choice_2B = False
choice_3A = False
choice_3B = False
choice_3C = False
choice_3D = False
result_4A = False #doctor
result_4B = False #ingredients
result_4C = False #usual
result_4D = False #special
result_4E = False #aardvark
result_4F = False #build
result_4G = False #buy
result_4H = False #broom
result_4I = False #cat
result_4J = False #noise
result_4k = False #bowl

#Start
print("""
Welcome to Zachs Choose your own adventure game 'BREAKFAST' 
To make a choice enter one of the capitalized words in the prompt and press enter.
""")

input("  Press ENTER to Start")

choice_1 = True

#Choice 1
while choice_1:
    breakfast = input("""
You wake up one morning,use the bathroom, get dressed, and read your scriptures.
You feel a bit hungry so you go to the kitchen to get some breakfast.

    --Do you make CEREAL or TOAST for breakfast?--    
    """).lower()

    if breakfast in ["cereal", "toast"]:
        if breakfast == "cereal":
            choice_1 = False
            choice_2A = True
            print('\n--CEREAL--\n')
        else:
            choice_1 = False
            choice_2B = True
            print('\n--TOAST--\n')
    else:
        print("Enter a valid answer.")
        continue

#Choice_2A -cereal
while choice_2A:
    meal = input("""
You open up the cupboards, grab a BOWL, and head to choose a cereal, but it turns out you have eaten almost all of the cereal and have not gone shopping for a while.
Only one mysterious cereal box remains, 'Finney Flakes', do you EAT the Finney Flakes, or go to the Aardvark CAFE on Hickory street?
    """).lower()

    if meal in ["eat", "cafe", "bowl"]:
        if meal == "eat":
            choice_2A = False
            choice_3A = True
            print('\n--EAT--\n')
        elif meal == 'bowl':
            choice_2A = False
            result_4k = True
            print('\n--BOWL--\n')
        else:
            choice_2A = False
            choice_3B = True
            print('\n--Cafe--\n')
    else:
        print("Enter a valid answer.")
        continue

#Choice_2B -toast
while choice_2B:
    shrew = input("""
You open the cupboard, grab a plate, and head to the bread box. You open the bread box and find a shrew eating all of your bread.
You stare at the shrew, the shrew stares back.

    Do you try to CATCH the shrew, or CHASE him out of your house?
    """).lower()

    if shrew in ["catch", "chase"]:
        if shrew == "catch":
            choice_2B = False
            choice_3C = True
            print('\n--CATCH--\n')
        else:
            choice_2B = False
            choice_3D = True
            print('\n--CHASE--\n')
    else:
        print("Enter a valid answer.")
        continue

#Choice 3A- EAT

while choice_3A:
    pick = input("""
You get and pour out the milk and take a bite. It tastes good, like corn flakes coated with butterscotch syrup.
You enjoy your meal and go about your day. However, for the rest of the day you see strange little dogs that no one else does and are really sensitive to smells.

    Do you go to the DOCTOR or go back to your house and take a better look at the INGREDIENTS that cereal box?
   """).lower()

    if pick in ["doctor", "ingredients"]:
        if  pick == "doctor":
            choice_3A = False
            result_4A = True
            print('\n--DOCTOR--\n')
        else:
            choice_3A = False
            result_4B = True
            print('\n--INGREDIENTS--\n')
    else:
        print("Enter a valid answer.")
        continue

#Choice 3B- CAFE
while choice_3B:
    order = input("""
You go to the cafe, are seated  by the hostess who looks suspiciously like an AARDVARK disguised as a  and receive a menu.
Your usual for breakfast is a "Big ole fat stack o' Pancakes with Sausage"

    When the waitress comes to take your order, do you order your USUAL, or get the daily SPECIAL?
   """).lower()

    if order in ["usual", "special", "aardvark"]:
        if  order == "usual":
            choice_3B = False
            result_4C = True
            print('\n--USUAL--\n')
        elif  order == "special":
            choice_3B = False
            result_4D = True
            print('\n--SPECIAL--\n')
        
        else:
            choice_3A = False
            result_4E = True
            print('\n--AARDVARK--\n')
    else:
        print("Enter a valid answer.")

#Choice_3C CATCH

while choice_3C:
    trap = input("""
You try to catch the shrew wih your hands, that ends miserably with you getting bit on the hand a bunch.
It is clear you will need a trap to catch the shrew. But how do you get one?
    Do you BUILD a trap using instructions found online? Or do you BUY one at the local hardware store?
   """).lower()

    if trap in ["build", "buy"]:
        if trap == "build":
            choice_3C = False
            result_4F = True
            print('\n--BUILD--\n')
        else:
            choice_3C = False
            result_4G = True
            print('\n--BUY--\n')
    else:
        print("Enter a valid answer.")
        continue

#Choice_3C CATCH

while choice_3D:
    option = input("""
You lunge at the shrew and chase the fiend out of the breadbox, but get your head stuck inside. After removing your cranium from the container,
you find the shrew has taken refuge in your cupboards, the question now is, what do you use to chase him out of there?

    Do you use a BROOM, a CAT, or a loud NOISE?
   """).lower()

    if option in ["broom", "cat", "noise"]:
        if option == "broom":
            choice_3D = False
            result_4H = True
            print('\n--BROOM--\n')
        elif option == "cat":
            choice_3D = False
            result_4I = True
            print('\n--CAT--\n')
        else:
            choice_3D = False
            result_4J = True
            print('\n--NOISE--\n')

    else:
        print("Enter a valid answer.")
        continue

#Endings/Results

if result_4A:
    print("""
You go to your doctor's office and get an emergency checkup,
after hearing you ate Finney Flakes he tells you that eating Finney Flakes gives you the senses of Finn the Dog, the cereal's namesake and mascot.
Hightening your sense of smell and allowing you to see all the strange invisble creatures that only dogs can see and bark at.
You leave with an exorbitantly high hospital bill because of all the medicare patients.
    
    --The End--
    """)
elif result_4B:
    print("""
You return home and track down the box of Finney Flakes, you find it and chase a shrew of the box. (How did it get in there?) You view the ingredients. 
It tells you that Finney Flakes grant you the senses of Finn the Dog, the cereal's namesake mascot.
Apparently for 24 hours after eating a bowl you will have hightened smell and the ability to see and hear all the strange creatures from other dimensions Finn barks at.
Good thing you didn't go to the doctor, you might have got an unnecessary hospital bill.

    --The End--
    """)
elif result_4C:
    print("""
You order your usual, the "Big ole stake o' Pancakes with Sausage" and while you are enjoying their fluffy goodness, you find a dead ant in the syrup.
Further confirming your suspicion the hostess is an AARDVARK.

    --The End--
    """)
elif result_4D:
    print("""
You order the daily breakfast special, termite pudding. It is a firm, chocolate pudding the color of dry soil. Scatterd about through it are salted termites and grains of sugar.
It is suprisingly delicious.

    --The End--
    """)
elif result_4E:
    print("""
    
    --Secret Ending--

You ask the waitress if the hostess is an aardvark. She is so suprised at your question she trips over a spoon somone dropped, revealing she is a bunch of pangolins
on stilts dressed as a human. The hostess and two busboys chuck you out of the resturaunt, in the process knocking off her face mask.
She is indeed a buch of aardvarks dressed as woman. You go home and ponder what just happened here.

    --The End?--
    """)
elif result_4F:
    print("""
After looking up instructions on how to build a shrew trap, you find what appears to be an effective trap using a shop vaccuum, a nylon stocking, and a can of sardines.
You attempt to build the trap, and while you are looking for a nylon stocking or viable substitute, a bunch shrew drive away on your lawn mower.
That's going to be costly to replace. At least you can try to salvage what remains of your bread now.
    --The End--
    """)
elif result_4G:
    print("""
    --Good Ending--

You spend all day shopping at the hardware super store, Wrenchmart, and by the time you return with a shrew trap, you find an army of shrews watching
a golf tournament on your TV. At this point you are so tired, you just plop down in the chair and watch it with them.
You fall asleep and wake up the next morning to find a tiny check from the shrews. It turns out they thought your house was an AirBnB.
You made 200 bucks!

    --The End--
    """)
elif result_4H:
    print("""
You get the broom and attempt to remove the varmit from your can cupboard. After sever unsucessful attempts, a bunch of shrews appear out of nowhere and after dueling you with a mop, throw you out of your house.
The only thing left to do is shuffle off to the Aardvark Cafe and console yourself with pancakes and wait for the shrews to leave.

    --The End--
    """)
elif result_4I:
    print("""
You convince you neighbors to let you borrow their cat, and send the furry mercenary in to rid you of the shrew.
But it appears the shrew was not alone, and when you see the cat agan, it is hogtied and thrown out the door.
You spend the rest of the day assisting your neighbor in taking their humilated and cranky cat to the vet to check for injuries.
The cat is fine, you be won't be invited over for dinner anytime soon.

    --The End--
    """)
elif result_4J:
    print("""
You find a comically large pair of cymbals you bought for cousin in marching band at a yardsale and forgot to give to them. You bang them around to get the shrew to leave, but all you do is give yourself a headache.
You try various other noises to scare and chase the shrew out to no avail. Eventually you give up and go to the store for asprin.
When you return the cymbals are in a tree and the shrew is gone.

    --The End--
    """)
elif result_4K:
    print("""

    --Secret Ending--
You try to eat a bowl and chip a tooth. Whhy would you do that? Did you just type bowl because I capitalized it to hint at a secret ending?

    --The End--
    """)
else:
    print("ERROR!")
