
def bubble_sort(arr):
  """
  look for adjacent indexes which are out of place and 
  interchange their elements until the entire array is sorted.
  """
  pass


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


def quicksort(arr):
  pass

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

def counting_sort(arr):
  pass


# Basic Test: Array of 9 ints from 1-10
basic_arr = []
print(bubble_sort(basic_arr))
print(insertion_sort(basic_arr))
print(quicksort(basic_arr))
print(dutch_national(basic_arr))
print(merge_sort(basic_arr))
print(counting_sort(basic_arr))

# Long Array: Array of 1000 ints from 1-100
long_arr = []
print(bubble_sort(long_arr))
print(insertion_sort(long_arr))
print(quicksort(long_arr))
print(dutch_national(long_arr))
print(merge_sort(long_arr))
print(counting_sort(long_arr))
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
double_array = []
print(bubble_sort(double_array))
print(insertion_sort(double_array))
print(quicksort(double_array))
print(dutch_national(double_array))
print(merge_sort(double_array))
print(counting_sort(double_array))