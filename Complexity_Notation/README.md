# Prime Number Algorithms

This project implements and analyzes various algorithms to find and count prime numbers. It includes:
1. **Naive Algorithm**
2. **Break Early Algorithm**
3. **Prime Factor Algorithm**
4. **Sieve of Eratosthenes**

Each algorithm is evaluated for its efficiency and performance. Visualizations help compare the results and showcase prime numbers up to a specified limit.

---

## How It Works

Prime numbers are natural numbers greater than 1 that are divisible only by 1 and themselves. This project explores multiple algorithms with different time complexities to find and count prime numbers efficiently.

### Algorithms

1. **Naive Algorithm**  
   - Checks divisibility for all numbers from 2 to \( n-1 \) for each candidate.
   - **Time Complexity:** \( O(n^2) \)  

2. **Break Early Algorithm**  
   - Optimized naive approach that stops checking divisors as soon as a factor is found.
   - **Time Complexity:** \( O(n^2) \)  

3. **Prime Factor Algorithm**  
   - Checks divisors only up to \( \sqrt{n} \), leveraging the property that if \( j \) divides \( n \), then \( n/j \) must also divide \( n \).
   - **Time Complexity:** \( O(n \sqrt{n}) \)  

4. **Sieve of Eratosthenes**  
   - Marks multiples of primes as non-prime, starting from the smallest prime.
   - **Time Complexity:** \( O(n \log(\log(n))) \)  

---

## Features

### Prime Number Visualization
- **Dot Representation**:  
  Prime numbers are visualized as dots on the x-axis. The size of each dot is inversely proportional to the number of primes found, ensuring smaller dots as more primes are plotted.

### Performance Comparison
- The project plots:
  1. **Number of Operations vs. \( n \)**: Tracks the computational cost for each algorithm.
  2. **Log-Log Plots**: Visualizes growth rates for complexity analysis.

---

## Example Usage

### Counting Primes
```python
from prime_algorithms import count_primes_up_to

n = 100  # Upper limit
num_primes, primes = count_primes_up_to(n)
print(f"The number of primes up to {n} is {num_primes}")
