"""
Jeffery Russell
10-6-18

File Containing Variations of Quick Sort
"""


def partition(data):
    """
    Partitions a list of data into three sections
    which are lower, equal, and equal to the pivot
    which is selected to be the last element in the
    list.
    """
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


def quickSortNormal(data):
    """
    This is the traditional implementation of quick sort
    where there are two recursive calls.
    """
    if len(data) == 0:
        return []
    else:
        less, equal, greater = partition(data)
        return quickSortNormal(less) + equal + quickSortNormal(greater)


def quick_sort_accumulation(data, a):
    """
    Implementation of quickSort which forces tail recursion
    by wrapping the second recursive in the tail positioned
    recursive call and added an accumulation variable.
    """
    if len(data) == 0:
        return a
    less, equal, greater = partition(data)
    return quick_sort_accumulation(less,
                                   equal + quick_sort_accumulation(greater, a))


def quicksort(data):
    """
    Wrapper function for quick sort accumulation.
    """
    return quick_sort_accumulation(data, [])



print quicksort([1,3,1,5,7,9,2,3,5,5,6])
