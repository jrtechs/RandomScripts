
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
        return float("infinity")
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
    if len(S) == 0:
        return 0

    # Calculate the current line's badness
    curBad = 0

    k = i
    while curBad > badnessLine(S, M, i, k):
        curBad = badnessLine(S, M, i, k)
        k = k + 1

    return max(curBad, badnessLine(S, M, k))



def minBadDynamic(S, M):
    """
    Write a procedure minBadDynamic that implements
    the function mb' using dynamic program-
    ming. It should take only two parameters: S and M

    :param S: List of words
    :param M: Max length of line
    """
    pass


def minBadDynamicChoice(S, M):
    """
    Write a procedure minBadDynamicChoice that implements
    the function mb 0 using dynamic
    programming. In addition to returning mb(S, M ), it
    should also return the choices made

    :param S: List of words
    :param M: Max length of line
    """
    pass


def printParagraph(S, M):
    """
    which takes two parameters: S and M that displays the words in S on
    the screen using the choices of minBadDynamicChoice.

    What is the asymptotic running time of your
    algorithm?

    :param S: List of words
    :param M: Max length of line
    """
    pass
