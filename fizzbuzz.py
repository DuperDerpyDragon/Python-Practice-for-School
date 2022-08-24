for i in range(1001):
    isDivisiableBy3 = i % 3 == 0
    isDivisiableBy5 = i % 5 == 0
    if isDivisiableBy3 and isDivisiableBy5:
        print("fizzbuzz")
    elif isDivisiableBy3:
        print("fizz")
    elif isDivisiableBy5:
        print("buzz")
    else:
        print(i)

    