import time
import random

def ins_sort(arr):
    arr = arr[:]
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge(left, right):
    merged = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

# Test input
test_input = [64, 34, 25, 5, 22]

print("Insertion Sort Result:", ins_sort(test_input))
print("Merge Sort Result:", merge_sort(test_input))

random_list = random.sample(range(1, 1000), 50)

# Time insertion sort
start_time = time.time()
ins_sorted = ins_sort(random_list)
print("Insertion sort time:", time.time() - start_time)

# Time merge sort
start_time = time.time()
merge_sorted = merge_sort(random_list)
print("Merge sort time:", time.time() - start_time)