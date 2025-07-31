class Employee:
    language = "Py"
    salary = 12000 # This is a class attribute

harry = Employee()
print(harry.language, harry.salary)
harry.name = "harry" # This is a class instance attribute

rohan = Employee()
rohan.name = "Rohan Roro Robinson"
print(harry.name, harry.language, harry.salary,)

# here name is object instance attribute and salary and language are class attributes
# as they directly belong to the class
