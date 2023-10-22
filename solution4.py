# Write a function that calculates the value of 'a' to the power of 'b'.

# For example if a=2 and b=4, then power(2,4) would be calculating 2^4=2*2*2*2 so the result would be 16.

def power(base,exp):
    # any number to the 0th power is equal to 1, example 2^0=1
    if exp==0:
        return 1
    else: 
        return base*power(base,exp-1)

a=3
b=2
# 3^2=3*3 so 9 is the expected output
print(power(a,b))