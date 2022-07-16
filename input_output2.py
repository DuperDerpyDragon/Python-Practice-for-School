x = input("What is your password?")
if(x=="cat"):

    y = input("How much time have you spent doing this?")
    if (int(y) > 10):
        print("Wow that is a lot!")
    print("You like doing "+ x +" and you have spent "+ y +" doing this")
else:
    print("Wrong Password, try again")