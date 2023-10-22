# Write a function that prints the natural numbers from 1 to n.

def natural_numbers(lowerNum, higherNum):
    if lowerNum > higherNum:
        return
    else:
        print(lowerNum)
        natural_numbers(lowerNum + 1, higherNum)

n=10
natural_numbers(1,n)
