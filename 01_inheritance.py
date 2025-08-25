class Employee:
    company = "ITC"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")


# class Programmer:
#     company ="ITC Infotech"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")
#
#     def showlanguage(self):
#         print(f"The name is {self.name} and she is a good with {self.language}")
#

class Programmer():
    company = "ITC Infotech"
    def showLanguage(self):
         print(f"The name is {self.name} and she is a good with {self.language}")

a = Employee()
b = Programmer()

print(a.company, b.company)