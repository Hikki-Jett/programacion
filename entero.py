# def filter_list(l):
#     'return a new list with the strings filtered out'
#     l2 = []
#     for x in l:
#         try:
#             x / 2
#             l2.append(x)
#         except TypeError:
#             ""              
#     return l2   

# l = [1, 2, "aasf", "1", "12", 123]

# print(filter_list(l))

def filter_list(l):
  'return a new list with the strings filtered out'
  return [x for x in l if type(x) is not str]

l = [2,"s",10,"w","222"]
print(filter_list(l))