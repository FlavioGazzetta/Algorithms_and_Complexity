# Algorithms and Complexity

This repository contains implementations and analyses of various algorithms categorized into three key areas:
1. **Complexity Notation** - Focused on prime counting algorithms.
2. **Divide and Conquer** - Includes the Merge Sort algorithm and related techniques.
3. **Introduction and Fibonacci** - Covers Fibonacci sequence computation and introductory algorithms.

---

## Directory Structure

### 1. Complexity Notation
This section explores different algorithms for counting prime numbers, analyzing their performance and complexity.

#### Files:
- **`Performance_Comparison_of_Prime_Counting_Algorithms_Naive_Break_Early_vs_Prime_Factor_vs_Sieve.py`**  
  Compares the performance of various prime counting algorithms: Naive, Break Early, Prime Factor, and Sieve of Eratosthenes.

- **`Performance_of_Break_Early_Algorithm.py`**  
  Analyzes the efficiency of the Break Early algorithm for prime counting.

- **`Performance_of_Prime_Factor_Algorithm.py`**  
  Evaluates the Prime Factor algorithm for finding primes.

- **`Performance_of_Sieve_of_Eratosthenes_Algorithm.py`**  
  Tests the performance of the Sieve of Eratosthenes for prime counting.

- **`Sieve_of_Erothenes_number_of_primes.py`**  
  Counts the number of primes using the Sieve of Eratosthenes and visualizes the results.

#### Key Features:
- Comparison plots for performance.
- Efficient implementations for counting primes.
- Visualization of operations vs. complexity growth.

---

### 2. Divide and Conquer
This section implements the **Merge Sort algorithm**, along with enhancements for debugging and correctness validation.

#### Files:
- **`Basic_Merge_Sort.py`**  
  Implements a basic recursive Merge Sort algorithm.

- **`Improved_Merge_Sort.py`**  
  Adds debugging tools and validation with `exactly_half_of` and `crazy_sum`.

- **`Assertion.py`**  
  Includes assertion-based validations for input integrity.

- **`Majority_element_in_A`**  
  Computes the majority element in a list using divide-and-conquer techniques.

#### Key Features:
- Recursive and iterative divide-and-conquer implementations.
- Debugging enhancements to ensure correctness.
- Majority element computation for advanced problem-solving.

---

### 3. Introduction and Fibonacci
This section covers the **Fibonacci sequence**, with multiple algorithms for computation and testing.

#### Files:
- **`fibbonaci.py`**  
  Implements various Fibonacci algorithms: recursive, memoized, iterative, and matrix exponentiation.

- **`fibbonaci_computation_test.py`**  
  Provides test cases to verify the accuracy of Fibonacci algorithms.

#### Key Features:
- Efficient computation of Fibonacci numbers for large \( n \).
- Comparison of runtime for different Fibonacci algorithms.
- Test cases to validate the implementations.

---

## Example Usage

### Complexity Notation
```bash
python Performance_Comparison_of_Prime_Counting_Algorithms_Naive_Break_Early_vs_Prime_Factor_vs_Sieve.py
