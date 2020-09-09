def smallestDifference(arrayOne, arrayTwo):
# Write your code here.
    minNum = arrayTwo[2]
    for i in range(len(arrayOne)):
        for j in range(len(arrayTwo)):
            difference = arrayOne[i] - arrayTwo[j]
            if difference >= 0 and difference < minNum:
                minNum = difference
                smallestValues = [arrayOne[i] , arrayTwo[j]]
    return smallestValues

print(smallestDifference([-1,5,10, 20, 28, 3], [26, 134, 135, 15, 17]))