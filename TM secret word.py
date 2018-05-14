import random

words = ["cat","dog","skate","Lacrosse","Hockey"]
hint1 = ["Puck","Ice","Ball","bark","meow"]
hint2 = ["paw","whiskers","fast","cold","grass"]
number = random.randint(0,4)
secretword = words[number]
guess = ""
counter = 0

while True:
    print("Guess the secret word!")
    print("Type 'hint1', 'hint2', 'length', 'first letter', 'last letter', or 'give up' if you need help.")
    guess = input ()
    counter +=1


    if guess == secretword:
        print("You win!")
        print("It took you " + str(counter) + " guesses.")
        break

    elif guess == "hint1":
        print(hint1[number])

    elif guess == "hint2":
        print(hint2[number])

    elif guess == "length":
        print( len(secretword)   )

    elif guess == "first letter":
        print ( secretword[0] )

    elif guess == "last letter":
        print( secretword[-1] )

    elif guess == "give up":
        print( "The secret word was " + secretword )
        break

    else:
        print("Try again.")
        counter += 1
        
    
