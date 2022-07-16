def add(i):
    return i+i
def add2(i):
    return add*2
for i in range(1000):
    value =  add2(i)
    print(str(i) + " " + str(value))