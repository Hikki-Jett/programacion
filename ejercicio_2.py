# Write a function which calculates the average of the numbers in a given list.

# Note: Empty arrays should return 0.

def find_average(numbers):
    g = 0
    c = 0
    for x in numbers:
        g += x
        c += 1
        print(x,c)
    if x == 0:
        return x
    else:
        return g/c
    
l = []

print(find_average(l))