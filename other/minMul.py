import math

"""
Jeffery Russell
11-12-18
"""


def generateMinOrdering(C, i, j):
    if i == j:
        return str(i)
    return "(" + generateMinOrdering(C, i, C[i -1][j -1]) + generateMinOrdering(C, C[i -1][ j -1] +1, j) + ")"



def minMul(S):
    """
    Simple function to print the matrixes used in
    the minimum matrix chain multiplication problem
    using dynamic programming.
    """
    n = len(S)
    m = [[math.inf for i in range(n)] for j in range(n)]
    c = [[0 for i in range(n)] for j in range(n)]

    for i in range(0, n):
        m[i][i] = 0
    
    for l in range(1, n + 1):
        for i in range(0, n-l + 1):
            j = l + i -1
            for k in range(i, j):
                temp = m[i][k] + m[k + 1][j] + S[i][0] * S[k][1] * S[j][1]
                print(temp)
                if temp < m[i][j]:
                    m[i][j] = temp
                    c[i][j] = k + 1


    for i in range(0, n):
        for y in range(0, n):
            print(str(m[i][y]) + " ", end =" ")
        print()


    print()
    print()
    for i in range(0, n):
        for y in range(0, n):
            print(str(c[i][y]) + " ", end =" ")
        print()

    print(generateMinOrdering(c, 1, len(S)))



"""
Makes sure that other programs don't execute the main
"""
if __name__ == '__main__':
    try:
        #minMul([(10,100),(100, 5),(5, 50)])
        minMul([(5,10),(10,3),(3,12), (12,5), (5,50), (50,6)])
        #minMul([(30,35),(35,15),(15,5), (5,10), (10,20), (20,25)])
    except KeyboardInterrupt:
        exit()