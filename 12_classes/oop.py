class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary
        
    def display_employee_details(self):
        print("Employee ID:", self.id)
        print("Employee Name:", self.name)
        print("Employee Salary:", self.salary)

    def print_all_employees():
        pass
    
class EmployeeManagementSystem:
    def __init__(self):
        self.employee_list = []
        
    def add_employee(self, employee):
        self.employee_list.append(employee)
        
    def remove_employee(self, employee_id):
        for employee in self.employee_list:
            if employee.id == employee_id:
                self.employee_list.remove(employee)
                return True
        return False
        
    def display_all_employees(self):
        for employee in self.employee_list:
            employee.display_employee_details()

# Usage
ems = EmployeeManagementSystem()

employee1 = Employee(1, "John Doe", 50000)
employee2 = Employee(2, "Jane Doe", 60000)

ems.add_employee(employee1)
ems.add_employee(employee2)

ems.display_all_employees()

ems.remove_employee(1)

ems.display_all_employees()



class Classname2():
    pass


a = [1,2,3]
a = list(1,2,3)
a = ClassName()