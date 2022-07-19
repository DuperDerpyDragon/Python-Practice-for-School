x = 1
while x == 1:
    userAnswer = input("What do you choose? (Rock, Paper, Scissors)? ")

    if userAnswer == "rock":
        print("Paper wraps rock")
    elif userAnswer == "paper":
        print ("Scissors cuts paper")
    elif userAnswer == "scissors":
        print("Rock crushes scissors")
    input("Good game, do you want to continue? (y/n)")
    if input != "y":
        break