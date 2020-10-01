"""
:Author: James Sherratt
:Date: 20/10/2019
:License: MIT

:name: heapsort.py

Heap sorts a list-like object. Note: this has been written with code-clarity
in mind first, efficiency second.
"""

from random import randint


def get_left(i):
    """
    Get the left element index of a heap node for an array.
    :param i: The parent index.
    :return: the left element.
    """
    return 2 * i + 1


def get_right(i):
    """
    Get the right element index of a heap node for an array.
    :param i: The parent index.
    :return: the right element.
    """
    return 2 * i + 2


def repair_heap(vals_list, root, arr_top):
    """
    Sifts the root element of a heap to the correct position, to
    correct a max heap. This assumes the children of the root/ node are max heaps.

    :param vals_list: list of values, which represents a heap structure.
    :param root: the index of the node we're working from/ using as a root.
    :param arr_top: the largest value of the list we're interested in.
    :return: Reference to the passed list, with the root node in the correct position.
    """
    # This is the value to swap. We want to swap the root value down, so we swap the root first.
    swap = root

    # Get left and right nodes of root.
    left = get_left(root)
    right = get_right(root)
    while left < arr_top:
        # Check if value to swap is less than the left child.
        if vals_list[swap] < vals_list[left]:
            swap = left
            # Check if value to swap is less than the right child (if exists).
            # Note: these 2 if's could be combined using "and", but then we're relying on lazy evaluation.
        if right < arr_top:
            if vals_list[swap] < vals_list[right]:
                swap = right
        # Check if the swap is still the root. If so, there's no more children to swap and we're done.
        if swap == root:
            return vals_list
        # Else, swap.
        else:
            vals_list[root], vals_list[swap] = vals_list[swap], vals_list[root]
            # New root, left and right node for the next iteration.
            root = swap
            left = get_left(root)
            right = get_right(root)

    return vals_list


def max_heap(vals_list):
    """
    Convert a list of values into a max heap tree.

    :param vals_list: list of numbers.
    :return: the same list as a max heap tree.
    """
    # Create a max heap by repairing the heap, starting from the nodes one above the leaf nodes.
    len_list = len(vals_list)
    for root in range(len_list//2, -1, -1):
        repair_heap(vals_list, root, len_list)

    return vals_list


def max_heap_to_sorted(vals_list):
    """
    Convert a max heap list into a sorted list.

    :param vals_list: list containing max heap.
    :return: the same list of values, sorted.
    """
    # i is the index of the last element of the slice of the array that needs sorting.
    for top in range(len(vals_list)-1, 0, -1):
        # Swap the root value (max) with the last value of the slice.
        vals_list[0], vals_list[top] = vals_list[top], vals_list[0]
        # Sift the new root to the correct position of the remainder of the max heap.
        # Another way of doing this is to pass a slice of the vals_list up to the value top, but python passes
        # slices by copy so there's a massive performance hit.
        repair_heap(vals_list, 0, top)

    return vals_list


def heapsort(vals_list):
    """
    Sort a list of values using heapsort.

    :param vals_list: list of sortable values.
    :return: the same list, sorted.
    """
    max_heap(vals_list)
    return max_heap_to_sorted(vals_list)


if __name__ == "__main__":
    list_len = 100000
    vals_list = [randint(0, (2**16)) for i in range(list_len)]
    heap_sorted = heapsort(list(vals_list))
    py_sorted = sorted(vals_list)
    print("Did the sort work? {}".format(heap_sorted == py_sorted))
