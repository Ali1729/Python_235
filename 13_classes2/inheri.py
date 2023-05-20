class Employee:
    def __init__(self, id, name, salary,role):
        self.id = id
        self.name = name
        self.salary = salary
        self.role = role
        
    def display_employee_details(self):
        print("Employee ID:", self.id)
        print("Employee Name:", self.name)
        print("Employee Salary:", self.salary)

    def increment(self):
        self.salary = self.salary * 1.10
        

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
            
    def increment(self):
        self.salary = self.salary * 1.10
# Usage
       
class Manager(Employee,EmployeeManagementSystem):
    
    pass
        

ems = EmployeeManagementSystem()

employee1 = Manager(1, "John Doe", 50000,"manager")
employee2 = Employee(2, "Jane Doe", 60000,"account")

ems.add_employee(employee1)
ems.add_employee(employee2)

ems.display_all_employees()

employee1.increment()
employee2.increment()
print("\n\n\n")
ems.display_all_employees()


