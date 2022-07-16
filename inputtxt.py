holder = ""
with open("input.txt") as f:
    contents = f.read()
    for c in contents:
            if c == " ":
                print(holder)
                holder = ""
            else:
                holder = holder + c
