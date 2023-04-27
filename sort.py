import numpy as np
import array


def bubble_sort(arr):
    """
    look for adjacent indexes which are out of place and 
    interchange their elements until the entire array is sorted.
    """
    while True:
        swaps = 0
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swaps += 1
        if swaps == 0:
            break
    return arr


def insertion_sort(arr):
    for i in range(len(arr)):
        mn = float('inf')
        mnj = i
        for j in range(i, len(arr)):
            if arr[j] < mn:
                mn = arr[j]
                mnj = j
        arr[i], arr[mnj] = arr[mnj], arr[i]
    return arr

# @TODO


def quicksort(arr):
    pass

# @TODO


def dutch_national(arr):
    pass


def merge_sort(arr):
    def ms_help(piece):
        if len(piece) <= 1:
            return piece
        a = ms_help(piece[:len(piece) // 2])
        b = ms_help(piece[len(piece) // 2:])
        return merge(a, b)

    def merge(arr1, arr2):
        result = []
        idx1 = 0
        idx2 = 0
        while len(arr1) > idx1 and len(arr2) > idx2:
            if arr1[idx1] < arr2[idx2]:
                result.append(arr1[idx1])
                idx1 += 1
            else:
                result.append(arr2[idx2])
                idx2 += 1
        while len(arr1) > idx1:
            result.append(arr1[idx1])
            idx1 += 1
        while len(arr2) > idx2:
            result.append(arr2[idx2])
            idx2 += 1
        return result

    return ms_help(arr)

# @TODO
def counting_sort(arr):
    pass


# Basic Test: Array of 9 ints from 1-10
basic_arr = np.random.randint(1, 10, size=10)
print(bubble_sort(basic_arr))
print(insertion_sort(basic_arr))
print(quicksort(basic_arr))
print(dutch_national(basic_arr))
print(merge_sort(basic_arr))
print(counting_sort(basic_arr))

# Long Array: Array of 1000 ints from 1-100
long_arr = np.random.randint(1, 100, size=1000)
print(bubble_sort(long_arr)[:20])
print(insertion_sort(long_arr)[:20])
print(quicksort(long_arr)[:20])
print(dutch_national(long_arr)[:20])
print(merge_sort(long_arr)[:20])
print(counting_sort(long_arr)[:20])
# Repeat Elements: Array with many repeating elements
repeat_elem = []
print(bubble_sort(repeat_elem))
print(insertion_sort(repeat_elem))
print(quicksort(repeat_elem))
print(dutch_national(repeat_elem))
print(merge_sort(repeat_elem))
print(counting_sort(repeat_elem))
# Empty Test: Empty Array
empty = []
print(bubble_sort(empty))
print(insertion_sort(empty))
print(quicksort(empty))
print(dutch_national(empty))
print(merge_sort(empty))
print(counting_sort(empty))

# Double Array: Array of 500 doublesrepeat_elem = []
double_array = np.random.rand(500)
print(bubble_sort(double_array))
print(insertion_sort(double_array))
print(quicksort(double_array))
print(dutch_national(double_array))
print(merge_sort(double_array))
print(counting_sort(double_array))
