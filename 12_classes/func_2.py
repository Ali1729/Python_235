def create_employee(id, name, salary,role):
    print("creating employee")
    return {"id": id, "name": name, "salary": salary,"role":role}

def add_employee(employees, employee):
    employees.append(employee)

def remove_employee(employees, employee_id):
    for employee in employees:
        if employee["id"] == employee_id:
            employees.remove(employee)
            return True
    return False

def get_first_name(employee):
    return employee["name"].split(" ")[0]

def get_last_name(employee):
    return employee["name"].split(" ")[1]

def display_all_employees(employees):

    for employee in employees:
        print("Employee ID:", employee["id"])
        print("Employee Name:", employee["name"])
        print("Employee Salary:", employee["salary"])
        print("Employee role:", employee["role"])

def increase_salary(employee):
    print("employees" ,str(employees))
    if employee["role"] != 'manager':
        employee["salary"]= employee["salary"]*1.10
    else:
        employee["salary"]= employee["salary"]*1.15


def increase_manager_salary(employee):
    employee["salary"]= employee["salary"]*1.15
    
# Usage
if __name__ =='__main__':
    employees = []

    employee1 = create_employee(1, "John Doe", 50000,"accountant")

    employee2 = create_employee(2, "Smith Ross", 60000,"manager")

    add_employee(employees, employee1)
    add_employee(employees, employee2)
    print("\n\n\n\n")
    # display_all_employees(employees)

    increase_salary(employee1)
    # increase_salary(employee2)
    # # print(remove_employee(employees, 2))
    # print("\n\n\n\n")
    # # display_all_employees(employees)

    # print(get_first_name(employee1))
    # print(get_last_name(employee1))



a = list([1,2,3])