import time

password = input("What is your password? ")
confirm = input("Are you sure [ " + password + " ] Is correct? ")
if confirm == "Yes":
    print("setting new password")
    print("loading, please be patient")
    time.sleep(3)
    print("Password Set")
else:
    print("Ok please restart process")