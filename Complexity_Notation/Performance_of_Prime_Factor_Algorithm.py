import numpy as np
import matplotlib.pyplot as plt

# Global variable to track operation counts
operation_count = 0

# Prime Factor Algorithm
def prime_factor_algorithm(n):
    global operation_count
    operation_count = 0  # Reset operation count

    def is_prime(n):
        global operation_count
        if n == 1:
            operation_count += 1  # Comparison
            return False
        for j in range(2, int(n**0.5) + 1):  # Check up to sqrt(n)
            operation_count += 1  # Loop comparison
            if n % j == 0:
                operation_count += 1  # Modulo operation
                return False
        return True

    count = 0
    for i in range(2, n + 1):
        operation_count += 1  # Loop comparison
        if is_prime(i):
            count += 1
            operation_count += 1  # Increment operation
    return count

# Performance analysis
N = np.arange(2, 101)  # Range of n values
operation_counts_prime_factor = []

# Collect operation counts for the Prime Factor Algorithm
for n in N:
    operation_count = 0
    prime_factor_algorithm(n)
    operation_counts_prime_factor.append(operation_count)

# Plot 1: Operations vs n
plt.figure(figsize=(8, 3), dpi=150)

# Subplot 1: Operations vs n
plt.subplot(121)
plt.plot(N, operation_counts_prime_factor, label="Prime Factor Algorithm")
plt.xlabel("n")
plt.ylabel("Number of Operations")
plt.title("Operations vs n (Prime Factor)")
plt.legend(loc="best")

# Subplot 2: Log-log plot
plt.subplot(122)
valid_indices = np.array(operation_counts_prime_factor) > 0  # Avoid log(0)
plt.plot(
    np.log(N[valid_indices]),
    np.log(np.array(operation_counts_prime_factor)[valid_indices]),
    label="Data"
)

# Best fit line
slope, intercept = np.polyfit(
    np.log(N[valid_indices]), np.log(np.array(operation_counts_prime_factor)[valid_indices]), 1
)
plt.plot(
    np.log(N[valid_indices]),
    slope * np.log(N[valid_indices]) + intercept,
    label=f"Best fit slope = {slope:.2f}"
)

plt.xlabel("log n")
plt.ylabel("log Operations")
plt.title("Log-Log Plot (Prime Factor)")
plt.legend(loc="best")
plt.tight_layout()
plt.show()
