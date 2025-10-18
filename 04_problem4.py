def divisible5(num):
    if num % 5 == 0:
        return True
    return False
a = [4659876541,4567542,79763,4634,59,60,7465,85,95]

f = list(filter(divisible5,a))
print(f)
