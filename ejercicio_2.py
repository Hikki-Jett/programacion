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
    
l = [1,2]

print(find_average(l))