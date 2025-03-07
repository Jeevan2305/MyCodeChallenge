# Implement encapsulation in a class.
class Employee:
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def set_employeeId(self, employeeId):
        self.employeeId = employeeId
    def get_employeeId(self):
        return self.employeeId
    def set_salary(self, salary):
        self.salary = salary
    def get_salary(self):
        return self.salary

employee = Employee()

name = input("Enter the Employee name : ")
employee_Id = input("Enter the Employee ID : ")
salary = input("Enter the Employee salary : ")

employee.set_name(name)
print(employee.get_name())
employee.set_employeeId(employee_Id)
print(employee.get_employeeId())
employee.set_salary(salary)
print(employee.get_salary())
