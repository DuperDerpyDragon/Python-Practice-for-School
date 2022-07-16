for i in range(30):    
    if i % 5 == 0 and i % 3 == 0:
        print("fizzbuzz")
    if i % 3 == 0 and i % 5 != 0:
        print("fizz")
    if i % 5 == 0 and i % 3 != 0:
        print("buzz")
    if i % 3 != 0 and i % 5 != 0:
        print(i)

for i in range(30):
    isDivisiableBy3 = i % 3 == 0
    isDivisiableBy5 = i % 5 == 0
    if isDivisiableBy3 and isDivisiableBy5:
        print("fizzbuzz")

    if isDivisiableBy3 and not isDivisiableBy5:
        print("fizz")

    if not isDivisiableBy3 and isDivisiableBy5:
        print("buzz")
        
    if not isDivisiableBy3 and not isDivisiableBy5:
        print(i)

for i in range(30):
    isDivisiableBy3 = i % 3 == 0
    isDivisiableBy5 = i % 5 == 0
    if isDivisiableBy3:
        if isDivisiableBy5:
            print("fizzbuzz")
        else: 
            print("fizz")
    else:
        if isDivisiableBy5:
            print("buzz")
        else: 
            print(i)