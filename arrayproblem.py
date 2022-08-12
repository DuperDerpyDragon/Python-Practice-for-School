import statistics

def numberInput():
    userInputs = []

    listInput = input("Enter your numbers (type done to end list): ")
    while listInput != "done":
        userInputs.append(int(listInput))
        listInput = input("Enter your numbers (type done to end list):" )


    print("Your list is", userInputs,)
    
    maxInput = max(userInputs)
    minInput = min(userInputs)
    inputMean = statistics.mean(userInputs)
    inputMedian = statistics.median(userInputs)
    inputCopied = userInputs.copy()
    inputSorted = inputCopied.sort()
    inputReversed = userInputs.copy()
    inputReversed.sort(reverse= True)
    inputSummed = sum(userInputs)
    inputDistinct = set(userInputs)
    inputLength = len(userInputs)

    print("Your highest input is",maxInput ,)
    print("Your lowest input is",minInput ,)
    print("Your mean for your inputs is",inputMean ,)
    print("Your median for your inputs is",inputMedian ,)
    print("Your list sorted is",inputCopied ,)
    print("Your input reversed is",inputReversed  ,)
    print("Your list summed together is",inputSummed ,)
    print("Your list's distint numbers are",inputDistinct ,)
    print("Your total amount of numbers in your list is",inputLength ,)

numberInput()