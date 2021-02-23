def removeEvens(x):
    total = x
    numPoppped = 0
    for i in range(0, len(x)):
        if total[i - numPopped] % 2 == 0 and total[ i - numPopped] !=0:
            total.pop(i - numPopped)
            numPopped = numPopped + 1
    return total

print(removeEvens([1,2,3,4,5,6,7,8,]))