from Person import *

class Employee(Person):

    def details(self, company):
        # print(self.__name, "работает в компании", company) # так нельзя, self.__name - приватный атрибут
        print(self.name, "работает в компании", company)


tom = Employee("Bob", 23)
tom.details("Google")
tom.age = 33
tom.display_info()