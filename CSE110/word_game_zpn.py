#Import
from random import randint

#Base Variables
_secrets = ("turkey", "cranberry", "family", "stuffing", "pumpkin", "gratitude", "thanks", "pilgrim", "november", "cassarole", "mayflower")
playing = True
game = False
#Begin Game
print("\nWelcome to Zach's Thanksgiving Word Guessing Game!\n")
print("\n It's Thanksgiving thmed with eleven possible answers, excluding Thanksgiving.")

while playing:
    #Game Variables
    secret_word = _secrets[randint(0,12)]
    hint = [] 
    for char in secret_word:
        hint.append("_")
    guess = ""
    g_count = 0
    
    game = True
    while game:
        #Make HInt
        p_hint = ""
        for char in hint:
            p_hint = p_hint + char + " "

        #give hint
        print(f"\nYour hint is: {p_hint}")
        guess = input("What is your guess? ").lower()
        g_count += 1
        #check guess

        if guess == secret_word:
            print(f"\nYour guess was correct!\nThe word is {secret_word}.\nIt took you {g_count} guesses.\n")
            game = False
        
        elif len(guess) != len(secret_word):
            print("Sorry, the guess must have the same amount of letters as the hint.")
            for letter in range(0, len(hint)):
                hint[letter] = "_"
            
            continue
        
        else:
            print("You guess was not correct.")
            
            for letter in range(0, len(guess)):
                
                if guess[letter] in secret_word:
                    if guess[letter] == secret_word[letter]:
                        hint[letter] = guess[letter].upper()
                    else:
                        hint[letter] = guess[letter].lower()
                else:
                    hint[letter] = "_"
            continue
    
    else:
        again = input("Play again? (yes/no) ").lower()

        if again == "yes":
            continue
        else:
            print("Goodbye")
            playing = False