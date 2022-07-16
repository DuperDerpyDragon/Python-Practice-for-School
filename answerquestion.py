question = "How are you? "
answer1 = "good"
answer2 = "bad"
returninput = "That's Good!"
returninput2 = "That's bad!"
returninput3 = "I do not understand"

if input(question) == answer1:
    print(returninput)
elif input() == answer2:
    print(returninput2)
elif input() != answer1 and answer2:
    print(returninput3)