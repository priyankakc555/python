#Create a class Person with instance attributes name and age. Create a method get_details in this class to print name and age. 
#Create another class Employee with attributes salary and designation and inherits 
#the Person class. Create a method get_details in this class to print name, age, salary and designation of 
#the Employee.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        return f"Name is {self.name} and age is {self.age}"


p1 = Person("Jon", 30)
print(p1.get_details())

class employee(person):
    def _init_(self,name,age,salary,designation):
        super()._init_(name,age)
        self.salary=salary
        self.designation=designation 

        def get_details(self):
            print(super().get_details())
            return(f"salary is{self.salary}and designation is{self.designatiom}")
        
        e1=Employee("Jane",24,34000,"Manager")
        print(e1.get_details())

        
        
