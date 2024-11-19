import numpy as np
import matplotlib.pyplot as plt

# Merge Sort implementation
def merge_sort(arr):
    if len(arr) <= 1:  # Base case: array is already sorted
        return arr

    # Split the array into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    sorted_arr = []
    i = j = 0

    # Compare elements from left and right halves
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    # Add remaining elements from left and right halves
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return sorted_arr

# Example arrays to test merge sort
arr1 = [1, 2, 3, 4, 27, 3, 2, 2, 2, 2, 2, 2, 3, 2, 1, 2, 3]
arr2 = [8, 9, 10, 10, 11, 10, 0]
arr3 = [9, 7, 1, 10, 5, 9, 9]

# Sort the arrays
sorted_arr1 = merge_sort(arr1)
sorted_arr2 = merge_sort(arr2)
sorted_arr3 = merge_sort(arr3)

# Print sorted arrays
print("Sorted Array 1:", sorted_arr1)
print("Sorted Array 2:", sorted_arr2)
print("Sorted Array 3:", sorted_arr3)
