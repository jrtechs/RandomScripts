import math

"""
Jeffery Russell
11-13-18
"""


def extraSpace(S, M, i, j):
    """
    Computes the number of extra characters at the end of
    the line.
    Between each word there is only once space.

    :param S: List of words
    :param M: Max length of line
    :param i: start word index
    :param j: end word index
    """
    extraSpaces = M - j + i
    for x in range(i, j + 1):
        extraSpaces -= len(S[x])
    return extraSpaces


def badnessLine(S, M, i, j):
    """
    Computes Line badness. This is the number of
    extra spaces or infinity if the length exceeds M

    :param S: List of words
    :param M: Max length of line
    :param i: start word index
    :param j: end word index
    """
    es = extraSpace(S, M, i, j)
    if es < 0:
        return math.inf
    return es


def minBad(S, M, i):
    """
    Computes the badness of a paragraph as the
    badness of the worst line in the paragraph not
    including the last line.

    *this is recursive

    :param S: List of words
    :param M: Max length of line
    :param i: start word index
    """
    if badnessLine(S, M, i, len(S) -1) != math.inf:
        return 0

    min = math.inf

    for k in range(i + 1, len(S)):
        end = minBad(S, M, k)
        front = badnessLine(S, M, i, k - 1)
        max = end if end > front else front
        min = min if min < max else max
    return min


def minBadDynamic(S, M):
    """
    Write a procedure minBadDynamic that implements
    the function mb' using dynamic program-
    ming. It should take only two parameters: S and M

    :param S: List of words
    :param M: Max length of line
    """
    cost = [math.inf for i in range(len(S))]

    for i in range(0, len(S)):
        if badnessLine(S, M, 0, i) != math.inf:
            cost[i] = badnessLine(S, M, 0, i)
            if i == len(S) -1:
                return 0 #Everything fit on one line
        else:
            min = math.inf
            for k in range(0, i):
                before = cost[k]
                after = badnessLine(S, M, k + 1, i)
                if i == len(S) -1 and badnessLine(S, M, k+1, i) != math.inf:
                    after = 0 # Last Line
                max = before if before > after else after
                min = min if min < max else max
            cost[i] = min
    return cost[len(S) -1]


def minBadDynamicChoice(S, M):
    """
    Write a procedure minBadDynamicChoice that implements
    the function mb' using dynamic
    programming. In addition to returning mb(S, M ), it
    should also return the choices made

    :param S: List of words
    :param M: Max length of line
    """
    cost = [math.inf for i in range(len(S))]

    # List of tuples indicating start/end indices of line
    choice = [[] for i in range(len(S))]

    for i in range(0, len(S)):
        if badnessLine(S, M, 0, i) != math.inf:
            cost[i] = badnessLine(S, M, 0, i)
            choice[i] = [(0, i)]
            if i == len(S) - 1:
                return 0, [(0,i)] # One line
        else:
            min = math.inf
            choiceCanidate = []
            for k in range(0, i): # Finds the optimal solution
                before = cost[k] # Previously computed minimum
                after = badnessLine(S, M, k + 1, i) # Badness of new slice
                if i == len(S) - 1 and badnessLine(S, M, k+1, i) != math.inf:
                    after = 0 # Last line
                max = before if before > after else after
                if min > max:
                    # Captures where slice is being taken
                    choiceCanidate = choice[k] + [(k+1, i)]
                    min = max
            choice[i] = choiceCanidate
            cost[i] = min
    return cost[len(S) -1], choice[len(S) -1]


def printParagraph(S, M):
    """
    which takes two parameters: S and M that displays the words in S on
    the screen using the choices of minBadDynamicChoice.

    What is the asymptotic running time of your
    algorithm?

    This program will run asymptotically in O(n^2) due
    to the characteristic of calculating the minBad
    for each sub sequence and then looping through a
    maximum of |S| to find the optimal solution.

    :param S: List of words
    :param M: Max length of line
    """
    cost, choice = minBadDynamicChoice(S, M)
    print()
    for i in range(0, len(choice)):
        for x in range(choice[i][0], choice[i][1] + 1):
            print(str(S[x]), end=" ")
        print()


print(minBadDynamicChoice(["aaa", "aaa"], 6))
printParagraph(["jjjjjj","aaa", "bb", "cc", "ff", "mm", "ddddd", "ddddd"], 6)

printParagraph(["jjjjjj"], 6)