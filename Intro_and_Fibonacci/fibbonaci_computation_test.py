def fib_table(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    table = [0] * (n + 1)
    table[0], table[1] = 0, 1
    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]
        print(table[i], end="\n\n")  # Adding two newlines after each print
    return table[n]

print(fib_table(1000000))  # Use parentheses here to call the function
