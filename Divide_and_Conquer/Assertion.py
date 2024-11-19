def exactly_half_of(x):
    assert x%2==0 # can only return exactly half if it's divisible by 2
    return x//2 # integer division

def crazy_sum(X):
    n = len(X)
    half_n = exactly_half_of(n)
    left_sum = sum(X[0:half_n])
    print("left sum: ", left_sum)
    right_sum = sum(X[half_n:2*half_n])
    print("Right sum: ", right_sum)
    return left_sum+right_sum



print("total sum: ",crazy_sum([1,2,3,4]))