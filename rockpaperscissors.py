from asyncore import loop


while True:
    userAnswer = input("What do you choose? (Rock, Paper, Scissors)? ")

    if userAnswer == "rock":
        print("Paper wraps rock")
    elif userAnswer == "paper":
        print ("Scissors cuts paper")
    elif userAnswer == "scissors":
        print("Rock crushes scissors")

    playAgain = input("Play again? (Y/N): ")
    if playAgain != "y":
        break