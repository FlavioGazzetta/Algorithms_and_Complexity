# Merge Sort and Divide-and-Conquer

This project explores the **Merge Sort algorithm** as an implementation of the **divide-and-conquer paradigm**. It includes enhancements like validation functions and debugging tools to ensure correctness and provide deeper insights into how the algorithm works.

---

## What is Merge Sort?

Merge Sort is a sorting algorithm that divides the input array into smaller subarrays, sorts them recursively, and then merges them back into a single sorted array.

### **How it Works**
1. **Divide**:  
   - Split the array into two halves.
   - Continue splitting recursively until each subarray contains one or zero elements.

2. **Conquer**:  
   - Sort the smaller subarrays.
   - Merge the sorted halves into a single sorted array.

3. **Combine**:  
   - Use the merge step to combine the sorted halves into a fully sorted array.

---

## Features of the Project

1. **Merge Sort Implementation**:
   - Implements the divide-and-conquer paradigm with recursion.
   - Includes a merge function to combine two sorted subarrays.

2. **Validation and Debugging**:
   - **`exactly_half_of`**: Ensures array splitting is valid by verifying divisibility by 2.
   - **`crazy_sum`**: Computes and prints the sums of the left and right halves of the array during recursion for debugging.

3. **Robustness**:
   - Handles arrays with uneven lengths gracefully.
   - Provides informative error messages for invalid inputs.

4. **Examples and Testing**:
   - Demonstrates the algorithm on multiple example arrays.
   - Prints sorted outputs for verification.

---

## Algorithms

### **Merge Sort**
```python
def merge_sort(arr):
    if len(arr) <= 1:  # Base case: array is already sorted
        return arr

    # Split the array into two halves
    mid = exactly_half_of(len(arr))
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left_half, right_half)
