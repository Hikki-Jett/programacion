# You will be given an array a and a value x. All you need to do is check whether the provided array contains the value.

# Array can contain numbers or strings. X can be either.

# Return true if the array contains the value, false if not.

def check(seq, elem):
    g = 0
    for x in seq:
        if x == elem:
            g += 1
        else:
            ''
    if g > 0:
        return True
    else:
        return False 