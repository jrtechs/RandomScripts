"""
Jeffery Russell
12-1-18
"""


def knapsack(V, W, capacity):
    """
    Dynamic programming implementation of the knapsack problem

    :param V: List of the values
    :param W: List of weights
    :param capacity: max capacity of knapsack
    :return: List of tuples of objects stolen in form (w, v)
    """
    choices = [[[] for i in range(capacity + 1)] for j in range(len(V) + 1)]
    cost = [[0 for i in range(capacity + 1)] for j in range(len(V) + 1)]

    for i in range(0, len(V)):
        for j in range(0, capacity + 1):
            if W[i] > j:  # don't include another item
                cost[i][j] = cost[i -1][j]
                choices[i][j] = choices[i - 1][j]
            else:  # Adding another item
                cost[i][j] = max(cost[i-1][j], cost[i-1][j - W[i]] + V[i])
                if cost[i][j] != cost[i-1][j]:
                    choices[i][j] = choices[i - 1][j - W[i]] + [(W[i], V[i])]
                else:
                    choices[i][j] = choices[i - 1][j]
    return choices[len(V) -1][capacity]


def printSolution(S):
    """
    Takes the output of knapsack and prints it in a
    pretty format.

    :param S: list of tuples representing items stolen
    :return: None
    """
    print("Thief Took:")
    for i in S:
        print("Weight: " + str(i[0]) + "\tValue: \t" + str(i[1]))

    print()
    print("Total Value Stolen: " + str(sum(int(v[0]) for v in S)))
    print("Total Weight in knapsack: " + str(sum(int(v[1]) for v in S)))


values = [99,1,1,1,1, 1,1]
weights = [5,1,2,3,4,5,1]
printSolution(knapsack(values, weights, 6))