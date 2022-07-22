import random
import time

def createAnswer():
    randomNumber = random.randint(1, 6)

    if (randomNumber == 1):
        return("Rock")

    elif (randomNumber == 2):
        return("Paper")

    elif (randomNumber == 3):
        return("Scissors")

    elif (randomNumber == 4):
        return("Lizard")

    elif (randomNumber == 5):
        return("Spock")

    elif (randomNumber == 6):
        return("Kevin")

def computerAnswer(userAnswer):
    randomNumber = random.randint(0, 1)
    
    if userAnswer == "Rock":
        if(randomNumber == 1):
            print("Paper wraps Rock")
        else:
            print("Spock vaporizes Rock")
    
    elif userAnswer == "Paper":
        if(randomNumber == 1):
            print("Scissors cuts Paper")
        else:
            print("Lizard eats Paper")
    
    elif userAnswer == "Scissors":
        if(randomNumber == 1):
            print("Rock crushes Scissors")
        else:
            print("Spock smashes Scissors")
    
    elif userAnswer == "Lizard":
        if(randomNumber == 1):
            print("Rock Smashes Lizard")
        else:
            print("Scissors decapitates Lizard")
    
    elif userAnswer == "Spock":
        if(randomNumber == 1):
            print("Sizard poisons Spock")
        else:
            print("Paper disproves Spock")

    elif userAnswer == "Kevin":
        randomNumber = random.randint(1, 5)
        if (randomNumber == 5):
            print("Kevin runs off with Scissors")

        elif (randomNumber == 4):
            print("Kevin eats Rock")

        elif (randomNumber == 3):
            print("Kevin attacks Spock")

        elif (randomNumber == 2):
            print("Kevin tears Paper")
            
        elif (randomNumber == 1):
            print("Kevin eats Lizard")

    else:
        print("who knows")

while True:
    answer = createAnswer()
    print(answer)
    computerAnswer(answer)
    time.sleep(0.1) 
    
#while True:
 #   userAnswer = input("What do you choose? (Rock, Paper, Scissors, Lizard, Spock, Kevin)? (Or type exit to quit) ")
  #  if userAnswer == "exit":
   #     break
    #computerAnswer(userAnswer)