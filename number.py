import random
import statistics

print("We are going to play a game. I will think of a number and you will guess it, then you will think of a number and I will guess it")

def computerInteger():
    computerNumber = random.randint(1, 100)
    while True:
        userGuess = int(input("What is your guess? "))
        if userGuess > computerNumber:
            print("Smaller")
        elif userGuess < computerNumber:
            print("Bigger")
        elif userGuess == computerNumber:
            print("Good job, you guessed it!")
            break

def userNumber():
        
    max = 100
    min = 0
    
    found = False
    print("Hey there think of a number and ill guess it")
    while not found:
        guess = int((max + min) / 2)

        print("Is your number.... ", guess)

        answer = input("Is this number bigger, smaller, or the same?")

        if answer == "bigger".lower():
            min = guess
        elif answer == "smaller".lower():
            max = guess
        elif answer == "same".lower():
            print("Thank you for playing with me!")
            found = True

computerInteger()
userNumber()