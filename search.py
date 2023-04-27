def binary_search(arr, elem):
    # search arr for elem and return index of elem
    low = 0
    high = len(arr) - 1
    mid = len(arr) // 2
    while high > low:
        if elem > arr[mid]:
            low = mid + 1
        elif elem < arr[mid]:
            high = mid - 1
        else:
            return mid
        mid = (low + high) // 2
    return -1

# @TODO
def search_matrix(matrix, elem):
    pass

# STRING SEARCH ALGORITHMS

# @TODO
def brute_force():
    pass

# @TODO
def z_algo():
    pass

# @TODO
def rabin_karp(text, pattern):
    pass


# STRING SEARCH TESTS
