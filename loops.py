def square(x):
    return x*x
def cube(x):
    return square(x)*x
for i in range(10):
    value = cube(i)
    print(str(i) + " = " +str(value))
    while value >= 0:
        if (value % 2 == 1):
            print(value)
        value = value-1