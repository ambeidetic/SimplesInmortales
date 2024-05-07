def bynMultiplier(numsArray, n):
    outputNums = []

    for number in numsArray:
        outputNums.append(number * n)
    
    return outputNums


result = bynMultiplier([1,2,3,4,5], 10)

print(result)