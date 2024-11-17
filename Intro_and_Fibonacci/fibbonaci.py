import matplotlib.pyplot as plt
import numpy as np
import time

def fake_function(n):
    time.sleep(0.0001 * n * n)  # Reduced delay for testing

def timeit(n):
    start = time.time()
    fake_function(n)
    end = time.time()
    return end - start

N = [0, 10, 20, 30, 40, 50]
T = [timeit(n) for n in N]

plt.plot(N, T)
plt.xlabel('n')
plt.ylabel('Time (s)')
plt.title('Time Complexity of fake_function')
plt.show()  # Ensure the plot is displayed
