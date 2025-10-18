from functools import reduce
# map eg
l = [1, 2, 3, 4, 5]

square = (lambda x: x * x)

sqList = map(square, l)
print(list((sqList)))

# filter eg

def even(num):
    if num % 2 == 0:
        return True

    return False

onlyEven = filter(even, l)
print(list(onlyEven))

# Reduce Eg

def sum(num1, num2):
    return num1 + num2

mul = lambda num1, num2: num1 * num2

print(reduce(sum, l))
print(reduce(mul, l))