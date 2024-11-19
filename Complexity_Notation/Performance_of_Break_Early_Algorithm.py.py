import numpy as np
import matplotlib.pyplot as plt

# Global variable to track operation counts
operation_count = 0

# Break Early Algorithm
def break_early_prime_count(n):
    global operation_count
    operation_count = 0  # Reset operation count

    def is_prime(x):
        global operation_count
        if x == 1:
            operation_count += 1  # Comparison
            return False
        for j in range(2, x):  # Check divisors up to x-1
            operation_count += 1  # Loop comparison
            if x % j == 0:
                operation_count += 1  # Modulo operation
                return False  # Break early
        return True

    count = 0
    for i in range(2, n + 1):
        operation_count += 1  # Loop comparison
        if is_prime(i):
            count += 1
            operation_count += 1  # Increment count
    return count

# Performance analysis
N = np.arange(2, 101)  # Range of n values
operation_counts_break = []

# Collect operation counts for the Break Early Algorithm
for n in N:
    operation_count = 0
    break_early_prime_count(n)
    operation_counts_break.append(operation_count)

# Plot 1: Operations vs n
plt.figure(figsize=(8, 3), dpi=150)

# Subplot 1: Operations vs n
plt.subplot(121)
plt.plot(N, operation_counts_break, label="Break Early Algorithm")
plt.xlabel("n")
plt.ylabel("Number of Operations")
plt.title("Operations vs n (Break Early)")
plt.legend(loc="best")

# Subplot 2: Log-log plot
plt.subplot(122)
valid_indices = np.array(operation_counts_break) > 0  # Avoid log(0)
plt.plot(
    np.log(N[valid_indices]),
    np.log(np.array(operation_counts_break)[valid_indices]),
    label="Data"
)

# Best fit line
slope, intercept = np.polyfit(
    np.log(N[valid_indices]), np.log(np.array(operation_counts_break)[valid_indices]), 1
)
plt.plot(
    np.log(N[valid_indices]),
    slope * np.log(N[valid_indices]) + intercept,
    label=f"Best fit slope = {slope:.2f}"
)

plt.xlabel("log n")
plt.ylabel("log Operations")
plt.title("Log-Log Plot (Break Early)")
plt.legend(loc="best")
plt.tight_layout()
plt.show()
