import random
import time

def createAnswer():
    randomNumber = random.randint(1, 5)

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

    else:
        print("who knows")

while True:
    answer = createAnswer()
    print(answer)
    computerAnswer(answer)
    time.sleep(0.5)
    


#while True:
 #   userAnswer = input("What do you choose? (Rock, Paper, Scissors, Lizard, Spock)? (Or type exit to quit) ")
  #  if userAnswer == "exit":
   #     break
    #computerAnswer(userAnswer)