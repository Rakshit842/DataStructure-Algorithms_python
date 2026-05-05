# Bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:   # already sorted, early exit
            break
    return arr

# Test
print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))
# Output: [11, 12, 22, 25, 34, 64, 90]


# selection sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap minimum to current position
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Test
print(selection_sort([64, 25, 12, 22, 11]))
# Output: [11, 12, 22, 25, 64]


# insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]       # element to be placed
        j = i - 1
        # Shift elements greater than key one position right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Test
print(insertion_sort([12, 11, 13, 5, 6]))
# Output: [5, 6, 11, 12, 13]


# Merge sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left  = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]);  i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Test
print(merge_sort([38, 27, 43, 3, 9, 82, 10]))
# Output: [3, 9, 10, 27, 38, 43, 82]


# Quick sort
def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
    return arr

def partition(arr, low, high):
    pivot = arr[high]   # last element as pivot
    i = low - 1         # index of smaller element
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Test
print(quick_sort([10, 7, 8, 9, 1, 5]))
# Output: [1, 5, 7, 8, 9, 10]


# Counting sort
def counting_sort(arr):
    if not arr:
        return arr

    max_val = max(arr)
    min_val = min(arr)
    k = max_val - min_val + 1

    # Step 1: count occurrences
    count = [0] * k
    for num in arr:
        count[num - min_val] += 1

    # Step 2: rebuild sorted array
    result = []
    for i, freq in enumerate(count):
        result.extend([i + min_val] * freq)
    return result

# Test
print(counting_sort([4, 2, 2, 8, 3, 3, 1]))
# Output: [1, 2, 2, 3, 3, 4, 8]
# k = range of values, n = number of elements