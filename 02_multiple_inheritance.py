class Employee:
    company = "ITC"
    name = "Default name"
    def show(self):
        print(f"The name is {self.name} and the company is {self.company}")

class Coder:
    language = "Python"
    def printlanguages(self):
        print(f"Out of all the languages here is your language :{self.language}")


class Programmer(Employee, Coder):
    company = "ITC Infotech"
    def showLanguage(self):
         print(f"The name is {self.company} and she is a good with {self.language}")

a = Employee()
b = Programmer()

b.show()
b.printlanguages()
b.showLanguage()
