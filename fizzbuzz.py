for i in range(31):
    isDivisiableBy3 = i % 3 == 0
    isDivisiableBy5 = i % 5 == 0
    if isDivisiableBy3 and isDivisiableBy5:
        print("fizzbuzz")