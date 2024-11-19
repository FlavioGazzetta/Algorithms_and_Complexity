import numpy as np
import matplotlib.pyplot as plt

# Global variable to track operation counts
operation_count = 0

# Naive Algorithm
def naive_num_primes_less_than(n):
    global operation_count
    operation_count = 0  # Reset operation count

    def is_prime(n):
        global operation_count
        if n == 1:
            operation_count += 1
            return False
        no_factors = True
        for j in range(2, n):
            operation_count += 1  # Loop comparison
            if n % j == 0:
                operation_count += 1  # Modulo operation
                no_factors = False
        return no_factors

    count = 0
    for i in range(2, n + 1):
        operation_count += 1  # Loop comparison
        if is_prime(i):
            count += 1
            operation_count += 1  # Increment operation
    return count

# Break Early Algorithm
def simplest_num_primes_less_than_break(n):
    global operation_count
    operation_count = 0

    def is_prime(n):
        global operation_count
        if n == 1:
            operation_count += 1
            return False
        for j in range(2, n):
            operation_count += 1
            if n % j == 0:
                operation_count += 1
                return False
        return True

    count = 0
    for i in range(2, n + 1):
        operation_count += 1
        if is_prime(i):
            count += 1
            operation_count += 1
    return count

# Prime Factor Algorithm
def simplest_num_primes_less_than_sqrt(n):
    global operation_count
    operation_count = 0

    def is_prime(n):
        global operation_count
        if n == 1:
            operation_count += 1
            return False
        for j in range(2, int(n**0.5) + 1):
            operation_count += 1
            if n % j == 0:
                operation_count += 1
                return False
        return True

    count = 0
    for i in range(2, n + 1):
        operation_count += 1
        if is_prime(i):
            count += 1
            operation_count += 1
    return count

# Sieve of Eratosthenes
def sieve_of_eratosthenes(n):
    global operation_count
    operation_count = 0

    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        operation_count += 1
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                operation_count += 1
                is_prime[j] = False

    return sum(is_prime)

# Comparison of Algorithms
N = np.arange(2, 101)  # Range of n values
operation_counts_naive = []
operation_counts_break = []
operation_counts_sqrt = []
operation_counts_sieve = []

# Collect operation counts for each algorithm
for n in N:
    operation_count = 0
    naive_num_primes_less_than(n)
    operation_counts_naive.append(operation_count)

    operation_count = 0
    simplest_num_primes_less_than_break(n)
    operation_counts_break.append(operation_count)

    operation_count = 0
    simplest_num_primes_less_than_sqrt(n)
    operation_counts_sqrt.append(operation_count)

    operation_count = 0
    sieve_of_eratosthenes(n)
    operation_counts_sieve.append(operation_count)

# Plot results
plt.figure(figsize=(10, 6), dpi=150)

plt.plot(N, operation_counts_naive, label="Naive")
plt.plot(N, operation_counts_break, label="Break Early")
plt.plot(N, operation_counts_sqrt, label="Prime Factor (√n)")
plt.plot(N, operation_counts_sieve, label="Sieve of Eratosthenes")

plt.xlabel("n")
plt.ylabel("Number of Operations")
plt.title("Performance Comparison of Prime Counting Algorithms")
plt.legend(loc="best")
plt.tight_layout()
plt.show()
