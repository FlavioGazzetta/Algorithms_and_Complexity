import numpy as np
import matplotlib.pyplot as plt
def simple_num_primes_less_than(n):
    def is_prime(n):
        if n==1:
            return False
        no_factors = True
        for j in range(2, n):
            if n%j==0:
                no_factors = False
        return no_factors
    count = 0
    for i in range(2, n+1):
        if is_prime(i):
            count += 1
    return count


print(simple_num_primes_less_than(1000))