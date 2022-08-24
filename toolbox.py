#Variable:
x = 1
#Example of a use of Variables:

for i in range (1,500):
    canBeDividedBy7 = i % 7 == 0
    #This Variable checks if the number is perfectly divisible by 7
    print(i)
    if canBeDividedBy7:
        print("This number, unlike others in this list, is a multiple of 7.")

#Function:
def exampleFunction1():
    print("Hello there, I hope you have a good day!")

#Example of a use of Functions:

def exampleFunction2():
        for i in range (1,500):
            canBeDividedBy7 = i % 7 == 0
            if canBeDividedBy7:
                print("This number is a multiple of 7.")
            else:
                print("This number is not a multiple of 7.")

exampleFunction2()

#Example of a use of Loops:
y = 1
while y == 1:
#While allows certain actions to run
    print("Hello there!")
    z = y+1
    if z == 1+1:
        break
        #break allows the while loop to stop


#Example of a use of Conditions:
for i in range (1,100):
    print(i)
    if i % 5 == 0:
    #if, else and elif are all conditions. You can check their equality through
        print("This number can be divided by 5")