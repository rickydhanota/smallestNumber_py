# Write a function that takes in two non-empty arrays of integers, finds the pair of numbers (one from each array) whos absolute difference is closest to zero, and returns an array containing these two numbers, with the number from the first array in the first position.
# can assume there is only one pair of numbers with the smallest difference


# Niave solution
# def smallestDifference(arrayOne, arrayTwo):
#     minNum = float("inf")
#     for i in range(len(arrayOne)):
#         for j in range(len(arrayTwo)):
#             difference = arrayOne[i] - arrayTwo[j]
#             if difference >= 0 and difference < minNum:
#                 minNum = difference
#                 smallestValues = [arrayOne[i] , arrayTwo[j]]
#     return smallestValues

def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    idxOne = 0
    idxTwo = 0
    smallest = float("inf")
    current = float("inf")
    smallestPair = []
    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        firstNum = arrayOne[idxOne]
        secondNum = arrayTwo[idxTwo]
        if firstNum < secondNum:
            current = secondNum - firstNum
            idxOne += 1
        elif secondNum < firstNum:
            current = firstNum - secondNum
            idxTwo += 1
        else:
            return [firstNum, secondNum]
        if smallest > current:
            smallest = current
            smallestPair = [firstNum, secondNum]
    return smallestPair

print(smallestDifference([-1,5,10, 20, 28, 3], [26, 134, 135, 15, 17]))