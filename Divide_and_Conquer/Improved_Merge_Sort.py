def exactly_half_of(x):
    """
    Returns exactly half of x, ensuring x is divisible by 2.
    """
    assert x % 2 == 0, "Input must be divisible by 2"
    return x // 2  # Integer division


def crazy_sum(X):
    """
    Computes the sum of the left and right halves of the list X,
    assuming the length of X is divisible by 2.
    """
    n = len(X)
    half_n = exactly_half_of(n)
    left_sum = sum(X[0:half_n])
    right_sum = sum(X[half_n:2*half_n])
    return left_sum + right_sum


def merge_sort(arr):
    """
    Sorts an array using the Merge Sort algorithm.
    """
    if len(arr) <= 1:  # Base case: array is already sorted
        return arr

    # Split the array into two halves
    mid = exactly_half_of(len(arr))
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Optional: Debugging with crazy_sum
    if len(arr) % 2 == 0:  # Only calculate crazy_sum if array has even length
        crazy_sum(arr)

    # Merge the sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    """
    Merges two sorted arrays into one sorted array.
    """
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


# Example arrays to test the improved merge sort
arr1 = [1, 2, 3, 4, 3, 2, 2, 2, 2, 2, 2, 3, 2, 1, 2, 3]
arr2 = [8, 9, 10, 10, 10, 12, 14, 16]
arr3 = [9, 7, 1, 10, 5, 9, 9, 8]

# Sort the arrays
sorted_arr1 = merge_sort(arr1)
sorted_arr2 = merge_sort(arr2)
sorted_arr3 = merge_sort(arr3)

# Print sorted arrays
print("Sorted Array 1:", sorted_arr1)
print("Sorted Array 2:", sorted_arr2)
print("Sorted Array 3:", sorted_arr3)
