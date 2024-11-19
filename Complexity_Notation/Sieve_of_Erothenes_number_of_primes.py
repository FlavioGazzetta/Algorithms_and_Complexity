import numpy as np
import matplotlib.pyplot as plt

def count_primes_up_to(n):
    # Step 1: Create a list to track prime status for numbers up to n
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers

    # Step 2: Implement the Sieve of Eratosthenes
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    # Step 3: Extract primes and their count
    primes = [i for i in range(n + 1) if is_prime[i]]
    return len(primes), primes

# Example usage
n = 50000  # Set the upper limit
num_primes, primes = count_primes_up_to(n)

# Print the number of primes
print(f"The number of primes up to {n} is {num_primes}")

# Inversely proportional dot size
dot_sizes = 200 / np.sqrt(np.arange(1, len(primes) + 1))  # Decrease size as index increases
dot_sizes = np.maximum(dot_sizes, 5)  # Ensure a minimum dot size of 5 for visibility

# Plotting primes with inversely proportional dot sizes
plt.figure(figsize=(10, 5), dpi=150)

# Plot primes as dots with varying sizes
plt.scatter(primes, [1] * len(primes), s=dot_sizes, color="blue", label="Primes")

# Plot settings
plt.title(f"Prime Numbers and Count up to {n} ({num_primes} primes)")
plt.xlabel("Numbers")
plt.ylabel("Prime Indicator")
plt.yticks([])  # Remove y-axis ticks for clarity
plt.axhline(1, color="gray", linestyle="--", alpha=0.5)  # Horizontal reference line
plt.legend(loc="best")
plt.tight_layout()
plt.show()
