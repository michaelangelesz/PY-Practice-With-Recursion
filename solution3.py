# Write a function that returns the nth elements in the Fibonacci Sequence.

# The Fibonacci Sequence is the series of numbers where the next number is found by adding up the two numbers before it: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
# For example, if n=4, then the result would be '2' and if n=2, the result would be '1'

def fibonacci(n):
    if n<=1:
        return n
    else:
        return(fibonacci(n-1)+fibonacci(n-2))

n=11
for i in range(n):
    print(fibonacci(i))