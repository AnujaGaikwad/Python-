try:
    a = int(input("Hey, Enter a number: "))
    print(a)

except ValueError as v:
    print("Hey")
    print(v)

else:
    print("I am inside else")