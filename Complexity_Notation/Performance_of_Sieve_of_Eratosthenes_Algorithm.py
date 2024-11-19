import numpy as np
import matplotlib.pyplot as plt

# Global variable to track operation counts
operation_count = 0

# Sieve of Eratosthenes algorithm
def sieve_of_eratosthenes(n):
    global operation_count
    operation_count = 0  # Reset operation count

    is_prime = [True] * (n + 1)  # Assume all numbers are prime
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers

    for i in range(2, int(n**0.5) + 1):  # Loop from 2 to sqrt(n)
        operation_count += 1  # Loop comparison
        if is_prime[i]:
            for j in range(i * i, n + 1, i):  # Mark multiples of i as non-prime
                operation_count += 1  # Marking a multiple
                is_prime[j] = False

    # Count the number of primes
    return sum(is_prime)

# Performance analysis
N = np.arange(2, 30001)  # Range of n values
operation_counts_sieve = []

# Collect operation counts for the Sieve algorithm
for n in N:
    operation_count = 0
    sieve_of_eratosthenes(n)
    operation_counts_sieve.append(operation_count)

# Plot 1: Operations vs n
plt.figure(figsize=(8, 3), dpi=150)

# Subplot 1: Operations vs n
plt.subplot(121)
plt.plot(N, operation_counts_sieve, label="Sieve of Eratosthenes")
plt.xlabel("n")
plt.ylabel("Number of Operations")
plt.title("Operations vs n (Sieve)")
plt.legend(loc="best")

# Subplot 2: Log-log plot
plt.subplot(122)
valid_indices = np.array(operation_counts_sieve) > 0  # Avoid log(0)
plt.plot(
    np.log(N[valid_indices]),
    np.log(np.array(operation_counts_sieve)[valid_indices]),
    label="Data"
)

# Best fit line
slope, intercept = np.polyfit(
    np.log(N[valid_indices]), np.log(np.array(operation_counts_sieve)[valid_indices]), 1
)
plt.plot(
    np.log(N[valid_indices]),
    slope * np.log(N[valid_indices]) + intercept,
    label=f"Best fit slope = {slope:.2f}"
)

plt.xlabel("log n")
plt.ylabel("log Operations")
plt.title("Log-Log Plot (Sieve)")
plt.legend(loc="best")
plt.tight_layout()
plt.show()
