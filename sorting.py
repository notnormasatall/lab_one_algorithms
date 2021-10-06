from time import *
from random import *
from copy import deepcopy
from pprint import pprint


def shell_sort(array):
    """
    Shell Sort.
    """
    comparisons = 0

    mid = len(array) // 2

    while mid > 0:

        for i in range(mid, len(array)):

            key = array[i]
            j = i

            while j >= mid and array[j - mid] > key:
                comparisons += 1
                array[j] = array[j - mid]
                j -= mid

            array[j] = key
            comparisons += 1

        mid = mid // 2

    return array, comparisons


def selection_sort(array):
    """
    Selection Sort.
    """

    comparisons = 0
    for i in range(len(array)):

        min_i = i
        for j in range(i+1, len(array)):

            comparisons += 1
            if array[min_i] > array[j]:
                min_i = j

        array[i], array[min_i] = array[min_i], array[i]

    return array, comparisons


def merge_sort(array):
    """
    Merge Sort.
    """
    comparisons = 0

    if len(array) > 1:
        mid = len(array)//2
        left = array[:mid]
        right = array[mid:]

        left_part = merge_sort(left)
        right_part = merge_sort(right)

        comparisons += left_part[1] + right_part[1]

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):

            comparisons += 1

            if left[i] < right[j]:
                array[k] = left[i]
                i = i+1

            else:
                array[k] = right[j]
                j = j+1

            k = k+1

        while i < len(left):
            array[k] = left[i]
            i = i+1
            k = k+1

            comparisons += 1

        while j < len(right):

            array[k] = right[j]
            j = j+1
            k = k+1

            comparisons += 1

    return array, comparisons


def insertion_sort(array):
    comparisons = 0

    for i in range(1, len(array)):
        key = array[i]
        j = i

        comparisons += 1
        while(j > 0 and array[j-1] > key):
            array[j] = array[j-1]
            j = j-1

            comparisons += 1

        array[j] = key

    return array, comparisons


def algorithms(array):
    print(selection_sort(array))
    print(insertion_sort(array))
    print(merge_sort(array))
    print(shell_sort(array))


if __name__ == "__main__":
    pass
