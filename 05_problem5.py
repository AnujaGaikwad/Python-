from functools import reduce

a = [61,45,73,34,59,6,174,85,95]
def greater (a, b):
    if a > b:
        return a
    return b

print(reduce(greater,a))

