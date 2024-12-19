class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    salary = 90
    def getSalary(self):
        return self.salary
    
ronak = Employee("Ronak", 324324234235443545254523)
print(ronak.name)
print(ronak.salary)

harry = Employee("Harry", 32324324234235443545254523)
print(harry.name)
print(harry.salary)