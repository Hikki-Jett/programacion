# In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

def filter_list(l):
    'return a new list with the strings filtered out'
    l2 = []
    for x in l:
        try:
            x / 2
            l2.append(x)
        except TypeError:
            ""              
    return l2 