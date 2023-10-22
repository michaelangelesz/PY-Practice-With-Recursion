# Write a program that takes a positive number as an argument and prints the numbers from n to zero.
# Before we begin coding, we want to break down this problem and think about it recursively.
# We want to define a function that takes a number, let's say n , prints it, and calls itself again with the value of n-1. The function will keep calling itself until the base case is met. One way to do this is to determine if the number is equal to 0 and when it is, stop the function. Think about what the base case and recursive case would be.

def count_down(n):

    # Base case
    if n==0:
        return
    
    # Recursive case
    else:
        print(n)
        count_down(n-1)

n=8
count_down(n)