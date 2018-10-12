def sortedHasSum(s, x):
    tempSum = 0
    for i in range(len(s) -1, -1, -1):
        if tempSum + s[i] <= x:
            tempSum += s[i]
        if(tempSum == x):
            return True
    return False


def hasSumHelper(s, x):
    if len(s) == 1:
        if x - s[0] >= 0:
            return x - s[0]
        else:
            return x
    elif len(s) == 0:
        return x;
    lower,equal,upper = partition(s)

    leftOver = hasSumHelper(upper, x)

    if len(equal) > 1:
        leftOver = hasSumHelper([equal[0]], leftOver)
        leftOver = hasSumHelper(equal[1::],leftOver)
    else:
        leftOver = hasSumHelper(upper, leftOver)

    return hasSumHelper(lower, leftOver)


def hasSum(s, x):
    return hasSumHelper(s, x) == 0


def partition(data):
    pivot = len(data) -1
    lower, equal, upper = [], [], []

    for i in range(0, len(data), 1):
        if data[i] > data[pivot]:
            upper.append(data[i])
        elif data[i] == data[pivot]:
            equal.append(data[i])
        else:
            lower.append(data[i])

    return lower, equal, upper

