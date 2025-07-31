class Demo :
    a =4

o = Demo()
print(o.a) # Prints class attributes because  instance attribute is not present
o.a = 0 # Instance attribute is set
print(o.a) # Prints the instance attribute because instant attribute is present
print(Demo.a) # Prints the class attribute
