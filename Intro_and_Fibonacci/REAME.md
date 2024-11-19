# Fibonacci Sequence Algorithms

This project implements and analyzes various algorithms to compute the Fibonacci sequence. The Fibonacci sequence is defined as:
- \( F(0) = 0 \)
- \( F(1) = 1 \)
- \( F(n) = F(n-1) + F(n-2) \) for \( n \geq 2 \)

---

## Features

### Algorithms Implemented

1. **Recursive Algorithm**  
   - Computes Fibonacci numbers using a simple recursive approach.  
   - **Time Complexity:** \( O(2^n) \)  
   - **Space Complexity:** \( O(n) \) due to recursion stack.  

2. **Memoized Recursive Algorithm**  
   - Optimizes the recursive approach by storing previously computed values in a dictionary.  
   - **Time Complexity:** \( O(n) \)  
   - **Space Complexity:** \( O(n) \).  

3. **Iterative Algorithm**  
   - Uses a loop to compute Fibonacci numbers efficiently without recursion.  
   - **Time Complexity:** \( O(n) \)  
   - **Space Complexity:** \( O(1) \).  

4. **Matrix Exponentiation**  
   - Computes Fibonacci numbers using matrix exponentiation for \( n \geq 2 \).  
   - **Time Complexity:** \( O(\log n) \)  
   - **Space Complexity:** \( O(1) \).  

---

## How It Works

### Recursive Algorithm
```python
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
